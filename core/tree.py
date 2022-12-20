#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:15:16 2022

@author: alain
"""

import sys
import itertools
from contextlib import contextmanager
import re

from pprint import pprint
import logging
logger = logging.getLogger('geonodes')

from geonodes.core import colors
from geonodes.core import context
from geonodes.core.socket import DataSocket
from geonodes.core.node import Node, GroupInput, GroupOutput, Frame, Viewer, SceneTime, Group
#from geonodes.nodes.classes import Geometry

from .arrange import arrange

from typing import Any

import bpy
import mathutils


NODE_STD_ATTRS = [
   '__doc__', '__module__', '__slots__', 'bl_description', 'bl_height_default', 'bl_height_max',
   'bl_height_min', 'bl_icon', 'bl_idname', 'bl_label', 'bl_rna', 'bl_static_type',
   'bl_width_default', 'bl_width_max', 'bl_width_min', 'color', 'dimensions', 'draw_buttons',
   'draw_buttons_ext', 'height', 'hide', 'input_template', 'inputs', 'internal_links',
   'is_registered_node_type', 'label', 'location', 'mute', 'name', 'output_template', 'outputs',
   'parent', 'poll', 'poll_instance', 'rna_type', 'select', 'show_options', 'show_preview',
   'show_texture', 'socket_value_update', 'type', 'update', 'use_clamp', 'use_custom_color',
   'width', 'width_hidden']

# =============================================================================================================================
# Groups

def call_group(name, **kwargs):
    return Group(name, **kwargs)

class Groups:
    def __init__(self, prefix=""):
        self.prefix = prefix
        
    @property
    def snake_prefix(self):
        return "" if self.prefix == "" else self.prefix.lower().replace(" ", "_") + "_"
    
    def name(self, name):
        return f"{self.prefix} {name}"
        
    def __getattr__(self, name):
        lname = (self.snake_prefix + name).lower()
        reads = []
        for tree in bpy.data.node_groups:
            comp = tree.name.lower().replace(' ', '_')
            reads.append(comp)
            if comp == lname:
                return lambda **kwargs: call_group(tree.name, **kwargs)

        raise Exception(f"Groups: Node group '{self.snake_prefix}{name}' ({lname}) not found in node_groups: {reads}")
        
    def clear(self):
        
        names = [tree.name for tree in bpy.data.node_groups]
        
        n = len(self.prefix)
        for name in names:
            if name[:n] == self.prefix:
                bpy.data.node_groups.remove(bpy.data.node_groups[name])
        
    

# =============================================================================================================================
# Nodes tree    

class Tree:
    """ Wrap a Blender NodeTree
    
    :param tree_name: Name of the tree (index in ``bpy.data.node_groups``)
    :param clear: delete the existing nodes
    :param group: the tree node is not for a Geometry Node modifier but for a Group
    :type tree_name: str
    :type clear: bool
    :type group: bool
    
    
    A tree class encapsulates a Blender NodeTree:
        
    .. code-block:: python

        blender_tree = tree.btree # The Blender NodeTree

    
    Nodes are created by data sockets methods. In case of an error, the user can see the state of
    the tree when the script stops.
    
    **Creation / closure**
    
    Once the tree is completed, the :func:`arrange` method tries to place the nodes in a readable shape.
    Hence, building a tree is made between the two instructions:
        
    - ``tree = Tree(tree_name)`` : creation / opening of the Blender NodeTree
    - ``tree.close()`` : arrange the nodes
    
    It is recommended to use the ``with`` context:
        
    .. code-block:: python

        with Tree("Geometry Nodes") as tree:
            # ... nodes creation

    
    **The TREE static property**
    
    The TREE static attribute of class Tree maintains the current active Tree, i.e. the tree into which
    creating the new nodes. There is only one single *open* tree at a time.
    The method :func:`activate` set the tree as the current one.
    At creation time, a Tree instance becomes the current one.
    
    **Layouts**
    
    For a better clarity of the resulting tree, it is possible to put the newly created nodes in a layout.
    At creation time, one can define both the layout label and color.
    The layout creation makes use of the ``with`` context (see :func:`layout`):
        
    .. code-block:: python

        with Tree("Geometry Node") as tree:
            
            # Nodes created here are placed directly on the tree background
            
            with tree.layout("Some tricky computation", color="green"):
                
                # Nodes created here are placed in the current layout
                
                with tree.layout("The most difficult part", color="red"):
                    
                    # Layouts can be imbricated
                    
            # Back to standard creation
    
    **Initialization**
    
    At initialization time, the existing nodes can be deleted or kept. Use ``clear=True``
    to erase all the existing nodes.
      
    The nodes which are kept are the ones which can not be configured by script, for instance
    the  *Float Curve* or  *ColorRamp* nodes. These nodes are reused when instancied in the script.
    This allows not to loose nodes tuning.
        
    """
    
    KEEPS = ['GeometryNodeImageTexture', 'GeometryNodeInputMaterial', 'GeometryNodeStringToCurves', 'ShaderNodeFloatCurve',
             'ShaderNodeFloatCurve', 'ShaderNodeValToRGB', 'ShaderNodeVectorCurve', 'FunctionNodeInputColor']
    
    TREE = None
    
    def __init__(self, tree_name, clear=False, group=False):
        
        if bpy.data.node_groups.get(tree_name) is None:
            bpy.data.node_groups.new(tree_name, type='GeometryNodeTree')

        self.btree = bpy.data.node_groups[tree_name]
        """ The geometry tree nodes"""
        
        self.btree.use_fake_user = True
        
        # ---------------------------------------------------------------------------
        # Capture the configuration of the nodes
        # TO BE IMPROVED!
        
        class ONode:
            def __init__(self, bnode):
                match = re.search(r"\[\s*(\d+)", bnode.name)
                if match is None:
                    self.index = bnode.name
                else:
                    self.index = int(match.group(1))
                self.name  = bnode.name
                self.label = bnode.label
                self.args  = self.get_args(bnode)
                
            def __str__(self):
                return f"<{self.name}: {self.label}>\n"

            def __repr__(self):
                return str(self)
            
            def get_args(self, bnode):
                a = []
                for socket in bnode.inputs:
                    if not socket.enabled:
                        continue
                    
                    if socket.links:
                        continue
                    
                    try:
                        value = socket.default_value
                    except:
                        continue
                        
                    name = socket.name.lower().replace(' ', '_')
                    if isinstance(value, str):
                        a.append(f"{name}='{value}'")
                    else:
                        a.append(f"{name}={value}")
                        
                for attr in dir(bnode):
                    if attr[:2] == '__' or attr in NODE_STD_ATTRS:
                        continue
                    
                    try:
                        value = getattr(bnode, attr)
                    except:
                        continue
                    
                    name = attr.lower().replace(' ', '_')
                    if isinstance(value, str):
                        a.append(f"{name}='{value}'")
                    else:
                        a.append(f"{name}={value}")
                        
                return ", ".join(a)
            
        self.previous = {}
        """ Keep a list of the existing nodes before removing them"""
        for bnode in self.btree.nodes:
            onode = ONode(bnode)
            self.previous[onode.index] = onode
            
        # ---------------------------------------------------------------------------
        # Clear the tree
        
        self.btree.links.clear()

        self.old_bnodes = []
        """ The old nodes which are not deleted"""
        
        if clear:
            self.btree.nodes.clear()
        else:
            rems = []
            for bnode in self.btree.nodes:
                if bnode.bl_idname in Tree.KEEPS:
                    self.old_bnodes.append(bnode)
                else:
                    rems.append(bnode)
                    
            for bnode in rems:
                self.btree.nodes.remove(bnode)
            del rems
            
        self.nodes  = []
        """ List of the created nodes"""
        self.node_id = 0
        """ Node id counter. Incremented at each node registration"""
        self.activate()

        self.capture_attributes = True
        """ Flag to capture the attributes or not (see :func:`check_attributes`)"""
        
        # ----- Layouts stack
        
        self.disable_layouts = False
        """ Just for fun"""
        
        self.layouts = []
        """ Stack of layouts (see :func:`layout`)"""
        self.util_color = "dark_green"
        """ Color code for internal layouts"""
        self.gene_color = "dark_orange"
        """ Color code for internal layouts"""
        self.auto_color = "dark_rose"
        """ Color code for internal layouts"""
        
        # ----- Input and outputs
        
        self.group_input  = GroupInput(check_input_geometry=not group)
        """ The 'Group Input' node"""
        self.group_output = GroupOutput(check_output_geometry=not group)
        """ The 'Group Output' node"""
        
        self.capture_inputs = True
        """ Flag for capture_inputs argument for layouts."""
        
        # ----- Scene
        
        self.scene_ = None

        # ----- Reset the colors carroussel
        
        colors.reset()
        
    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.close()
        
    def __str__(self):
        return f"<Tree {self.btree.name} with {len(self.nodes)} nodes and {len(self.btree.links)} links>"
        
    # ----------------------------------------------------------------------------------------------------
    # Get / create a Blender node
        
    def get_bnode(self, bl_idname, label=None):
        """ Get an existing, or create a new, Blender node in the tree.
        
        :param bl_idname: The node bl_idname
        :param label: Node label
        :type bl_idname: str
        :type name: str
        :return: A geometry node
        :rtype: bpy.types.GeometryNode
        
        
        At initialization time, some nodes (the ones which can be changed by UX) are kept
        in ``old_bnodes`` list. Before creating a new node, this list is scaned to find a node
        of the proper type and the proper label.
        """
        
        found = None
        for bnode in self.old_bnodes:
            if bnode.bl_idname == bl_idname:
                if label is None:
                    found = bnode
                    break
                elif bnode.label == label:
                    found = bnode
                    break

        if found is None:
            bnode = self.btree.nodes.new(bl_idname)
            # Group: the label is used to pass the group name
            if bl_idname == 'GeometryNodeGroup':
                bnode.node_tree = bpy.data.node_groups.get(label)
        else:
            bnode = found
            self.old_bnodes.remove(bnode)
        
            if label is not None:
                bnode.label = label
            
        bnode.select = False
        bnode.parent = self.cur_frame
        
        return bnode
                        
        
    def activate(self):
        """ Set this tree as the current one.
        
        The Tree class property ``TREE`` is set to ``self``
        """
        
        Tree.TREE = self
        context.tree = self
        
    def register_node(self, node):
        """ Register the node passed in parameter in the current tree.
        
        :param node: The node to register
        :type node: Node
        :return: The node
        :rtype: Node
        
        When registered, a unique id is provided to the node.
        This allows the users to more clearly distinguish the nodes.
        
        """
        
        self.node_id += 1
        node.node_id = self.node_id
        self.nodes.append(node)
        return node
    
    # ---------------------------------------------------------------------------
    # Get the node wrapper of a blender node
    
    def get_bnode_wrapper(self, bnode):
        """ Get the Node instance wrapping the Blender node passed in argument.
        
        :param bnode: The geometry node to look the warpper of
        :type bnode: bpy.types.NodeSocket
        :return: The wrapping node
        :rtype: Node
        :raise: Exception if the wrapper is not found
        """
        
        for node in self.nodes:
            if node.bnode == bnode:
                return node
        raise Exception(f"Impossible to find the wrapper node of Blender node {bnode}.")
            
    def get_bsocket_wrapper(self, bsocket):
        """ Get the DataSocket instance wrapping the Blender socket passed in argument.
        
        :param bsocket: The blender socket to search the werapper of
        :type bsocket: bpy.types.NodeSocket
        :return: The node wrapping the socket
        :rtype: Node
        :raise: Exception if not found
        
        """
        
        node = self.get_bnode_wrapper(bsocket.node)
        for socket in itertools.chain(node.inputs, node.outputs):
            if socket.bsocket == bsocket:
                return socket
        raise RuntimeError(f"Impossible to find the wrapper socket of Blender socket {bsocket}, of node {node}.")
        
    # ----------------------------------------------------------------------------------------------------
    # Input output interface
    
    @property
    def input_geometry(self):
        """ The group input geometry.
        
        .. code-block:: python
        
            my_geometry = tree.input_geometry
        
        """
        return self.group_input.input_geometry
    
    @property
    def ig(self):
        """ Shortcut for :attr:`input_geometry`
        """
        return self.input_geometry
        
    @property
    def output_geometry(self):
        """ The group output geometry.
        
        .. code-block:: python
        
            tree.output_geometry = my_geometry 
        
        """
        return self.group_output.output_geometry
    
    @output_geometry.setter
    def output_geometry(self, value):
        self.group_output.output_geometry.plug(value)
        
    @property
    def og(self):
        """ Shortcut for :attr:`output_geometry`.
        """
        return self.output_geometry
        
    @og.setter
    def og(self, value):
        self.output_geometry = value
        
        
    def new_input(self, class_name, value=None, name=None, min_value=None, max_value=None, description=""):
        """ Create a new input socket.
        
        :param class_name: Class name of the value to get
        :param value: Initial value
        :param min_value: Minimum value
        :param max_value: Maximum value
        :param description: User type
        :type class_name: str
        :type value: Depending on the class
        :type min_value: Depending on the class
        :type max_value: Depending on the class
        :type description: str
        :return: A data socket
        :rtype: As defined by class_name
        
        .. code-block:: python
        
            res = tree.new_input('Integer', 10, "Resolution", min_value=2, max_value=100, descriptioo="Grid resolution")
        
        Don't use it directly, better call the constructor ``Input`` of data classes.
        
        .. code-block:: python
        
            res = Integer.Input(10, "Resolution", min_value=2, max_value=100, descriptioo="Grid resolution")
            
        """
        
        return self.group_input.new_socket(class_name=class_name, value=value, name=name, min_value=min_value, max_value=max_value, description=description)
    
    def to_output(self, socket):
        """ Create a new output socket linked to the data class.
        
        :param socket: The data socket to plug as group output
        :type socket: DataSocket

        .. code-block:: python
        
            tree.to_output(value)
        
        Don't use it directly, better call method ``to_output`` of data classes.
        
        .. code-block:: python
        
            value.to_output()

        """

    # ----------------------------------------------------------------------------------------------------
    # New in / out groups
    
    def new_group_input(self):
        """ Create a new instance in group input."""
        return GroupInput(check_input_geometry=False)
    
    def new_group_output(self):
        """ Create a new instance in group output."""
        return GroupOutput(check_output_geometry=False)
        
        
    # ----------------------------------------------------------------------------------------------------
    # Viewer
    
    def view(self, geometry=None, socket=None, domain='AUTO', label=None, node_color=None):
        """ Connect a data socket to the viewer.
        
        :param geometry: The geometry to connect to the viewer
        :param socket: The attribute to connect to the viewer
        :param domain: Geometry domain
        :type geometry: Geometry
        :type socket: Value
        :type domain: str
        
        You can also call ``DataSocket.view()``
        
        """
        
        viewer = Viewer(domain=domain, label=label, node_color=node_color)
        
        viewer.plug_socket(geometry)
        viewer.plug_socket(socket)
        
        return viewer
        
    # ----------------------------------------------------------------------------------------------------
    # Scene
    
    @property
    def scene(self):
        """ Maintain a single instance of the node :class:`SceneTime`.
        """
        if self.scene_ is None:
            self.scene_ = SceneTime()
        return self.scene_
        
    @property
    def frame(self):
        """ The "Scene Time" output socket "frame".
        
        Used for animation:

        .. code-block:: python
        
            with Tree("Geometry Nodes") as tree:
                height = tree.frame / 10 # a value which is a tenth of the current frame 
            
        """
        return self.scene.frame
    
    @property
    def seconds(self):
        """ The "Scene Time" output socket "seconds".
        
        Used for animation:
            
        .. code-block:: python
        
            with Tree("Geometry Nodes") as tree:
                time = tree.seconds.sqrt() # a value which is the square root of the time

        """
        return self.scene.seconds

    # ----------------------------------------------------------------------------------------------------
    # Layouts
    
    @contextmanager
    def layout(self, label="Layout", color=None, capture_inputs=None):
        """ Create a new layout where the newly created nodes will be placed.
        
        :param label: The layout label
        :param color: The color of the layout
        :param capture_inputs: Create a new instance fo group inputs in the frame
        :type label: str
        :type color: triplet, str or mathutils.Color
        :type capture_inputs: bool or None
        
        To be used in a `with` block:
            
        .. code-block:: python
        
            with tree.layout("My layout"): # Create a layout
                mesh = Mesh.UVSphere() # The node is parented in the layout
                
            mesh.set_shade_smooth() # "Set Shade Smooth" node is created in the tree backrgound

        """
        
        if isinstance(color, str):
            if color.upper() == 'UTIL':
                color = self.util_color
            elif color.upper() == 'GENE':
                color = self.gene_color
            elif color.upper() == 'AUTO':
                color = self.auto_color
                
        if self.disable_layouts:
            try:
                yield False
            finally:
                pass
            
        else:
            try:
                layout = Frame(label=label, color=color)
                self.layouts.append(layout)
                yield layout
                
            finally:
                frame = self.layouts.pop()
                if capture_inputs is None:
                    capture_inputs = self.capture_inputs
                frame.ok_capture_inputs = capture_inputs
            
    @property
    def cur_frame(self):
        """ Get the current layout for the newly created nodes.
        """
        if self.layouts:
            return self.layouts[-1].bnode
        else:
            return None
    
    # ----------------------------------------------------------------------------------------------------
    # Custom group
    
    def call(self, name, **kwargs):
        return Group(name, **kwargs)
    
    # ----------------------------------------------------------------------------------------------------
    # Insert a node in existing links
    # Args:
    # - node: the node to insert
    # - cut_links: list of dict
    #   - output_socket : blender output socket where to insert the new node
    #   - node_input    : name or index of the input socket of new node
    #   - node_output   : name or index of the output sockt of the new node
    
    def insert_node(self, node, cut_links):
        
        def s_socket(bsock):
            if bsock.is_output:
                s0 = "]"
                s1 = ">>>"
            else:
                s0 = ">>>"
                s1 = "["
            return f"{s0}{bsock.node.name}.{bsock.name} ({bsock.bl_idname}){s1}"
        
        def s_link(link):
            if link is None:
                return "None"
            else:
                return f"LINKS({s_socket(link.from_socket)} --> {s_socket(link.to_socket)})"
        
        for cut_link in cut_links:
            
            bout_socket = cut_link['output_socket']
            links = [link for link in bout_socket.links]
            
            index = cut_link['node_input']
            if isinstance(index, str):
                index = node.insockets.get(index)
            bnode_in_socket = node.bnode.inputs[index]
                
            index = cut_link['node_output']
            if isinstance(index, str):
                index = node.outsockets.get(index)
            bnode_out_socket = node.bnode.outputs[index]
            
            targets = []
            for link in links:
                targets.append(link.to_socket)
                self.btree.links.remove(link)

            self.btree.links.new(bout_socket, bnode_in_socket)
            
            for target in targets:
                self.btree.links.new(bnode_out_socket, target)
            
        return node
    
    # ----------------------------------------------------------------------------------------------------
    # Check attributes
    
    def check_attributes(self):
        """ Check the attributes
        
        This utility function is called when closing the tree to "solve" the attribute input nodes,
        i.e. to determine if a 'Capture Attribute' node is required.
        
        In **geonodes**, attributes are initialized as properties of a geometry.
        For instance, in the following piece of code, the node 'Position' is to be the *position*
        of the vertices of my_mesh:
            
        .. code-block:: python
        
            v = my_mesh.verts.position  # Create the node 'Position'
            
        To actually get these vertices, a 'Capture Attribute' can be necessary. This is determined
        by `check_attribute` method.
        
        The insertion is made with the following algorithm
        
        1. Check if capture is needed
        
           for each fed node:
               
           - if the node has an input geometry:
               
             - if the input geometry is the expected one:
                 
               - ok
               
             - else
             
               - insertion is needed
               
           - else:
               
             - continue exploration with the nodes fed by this node
        
        2. If insertion is needed
        
           - Create the 'Capture Attribute' node
           - Set the proper parameters
           - Input geometry with the owning socket
           - Output geometry to the sockets the owning socket was linked to
           - Output attribute to the sockets the attribute was connected to
           
         
        Note that by initializing an attribute with geometry and domain, we have what we need to insert
        a 'Capture Attribute' node:
            
        .. code-block:: python
        
            # Get the position of the vertices of my_mesh
        
            v = my_mesh.verts.position
            
            # Create the capture node
            
            capture_node = nodes.CaptureNode(
                geometry  = my_mesh,
                value     = (output socket of Position node),
                data_type = 'VECTOR',  # We deal with position which is a Vector
                domain    = 'POINT',   # my_mesh.verts.position  --> 'POINT'
                                       # my_mesh.edges.position  --> 'EDGE'
                                       # my_mesh.faces.position  --> 'FACE'
                )
           
        """
        
        # Flag to colorize the dependancies
        track_nodes = False
        
        from geonodes.nodes.classes import Geometry
        
        # ====================================================================================================
        # Get all the attribute nodes requiring the insertion of capture attribute node
        
        attr_nodes  = []
        path_tracks = [] # Tracking
        
        for attr_node in self.nodes:
            
            if not attr_node.is_attribute:
                continue
            
            # ---------------------------------------------------------------------------
            # ----- Check if the fed nodes with geometry input are ok
            
            security   = []
            fed_nodes  = [] # tracking: nodes explored forward
            end_nodes  = [] # trackin:  nodes with an input geometry socket
            geometries = [] # tracking: node feeding end nodes
            
            def check_geo_nodes(node):
                
                # ----- Loop on the nodes which are fed by the current node
                
                for nd in node.fed_nodes:
                    
                    # Keep track of the fed nodes
                    
                    if nd not in fed_nodes:
                        fed_nodes.append(nd)
                            
                    # Get the input geometry socket of the fed node
                    
                    in_geo_socket = nd.input_geometry_bsocket

                    logging.debug("CHECKING", attr_node, nd, '-->', in_geo_socket)
                    
                    # ---------------------------------------------------------------------------
                    # If no geometry socket, we continue twoards the fed nodes of this node
                    # Do avoid infinite loop, we keep track of the nodes with the security list

                    if in_geo_socket is None:

                        # Already explored
                        if nd in security:
                            continue
                        
                        # We do it once
                        security.append(nd)
                        
                        # A dead end, we quit
                        if not check_geo_nodes(nd):
                            return False
                        
                    # ---------------------------------------------------------------------------
                    # There is an input geometry socket
                    # We can move backwards to the feeding node
                        
                    else:
                        
                        # Keep track of path ends
                        if nd not in end_nodes:
                            end_nodes.append(nd)
                            
                        # Back to the feeding geometry
                        for link in in_geo_socket.links:
                            
                            # Keep track of the feeding geometry
                            try:
                                geometries.append(self.get_bnode_wrapper(link.from_node))
                            except:
                                pass
                                
                            # The input socket is the owning socket of the attribute
                            # Nothing to do : we return False to to stop the capture attribute node insetion
                            
                            if link.from_socket != attr_node.owning_bsocket:
                                return False
                            
                # If we didn't find the input geometry equal to the owning bsocket
                # we must insert a capture attribute node
                
                return True
            
            # ----- True if we need to insert an capture attribute node
                        
            if check_geo_nodes(attr_node):
                continue
            
            # ----- Let's memorize all this struff
            
            attr_nodes.append(attr_node)
            path_tracks.append({
                'fed_nodes': fed_nodes,
                'end_nodes': end_nodes,
                'geometries': geometries,
                })
            
        # ====================================================================================================
        # Loop on the attribute nodes requiring the insertion of a capture attribute node        
            
        for attr_node, path_track in zip(attr_nodes, path_tracks):
            
            # ---------------------------------------------------------------------------
            # ----- Context information to help in case of an error
            
            fed_nodes  = path_track['fed_nodes']
            end_nodes  = path_track['end_nodes']
            geometries = path_track['geometries']
            
            if track_nodes:
                for nd in fed_nodes:
                    nd.node_color = "cyan"
                for nd in end_nodes:
                    nd.node_color = "blue"
                for nd in geometries:
                    nd.node_color = "orange"
                    
                attr_node.node_color = "red"
                
            # ---------------------------------------------------------------------------
            # We insert a capture node on the output of the owning sockets
            # We need:
            # - The attribute socket
            #   - Will be plugged as attribute in the capture attribute node
            #   - The links we be moved at the output of the capture node
            # - The geometry
            #   - As geometry input of the capture attribute node
            #   - The links we be moved at the output of the capture node
            
            # One loop per output socket
            
            if True:
                
                # Debug
                # fprint = context.dump_tree(self.btree)
                
                out_geometry = attr_node.owning_bsocket
                
                for bsocket in attr_node.bnode.outputs:
    
                    links = bsocket.links
                    if len(links) == 0:
                        continue
                    
                    # ----- Create the capture node with the proper type
                    
                    data_type = DataSocket.value_data_type(bsocket, 'FLOAT')
                    capt_node = Geometry(attr_node.owning_bsocket).capture_attribute_node(data_type=data_type, domain=attr_node.domain)
                    
                    # ----- The index of the output socket depends upon the data type
                    
                    for i in range(1, len(capt_node.bnode.outputs)):
                        if capt_node.bnode.outputs[i].enabled:
                            sock_index = i
                            break
                    
                    cut_links = [
                        {'output_socket': out_geometry, 'node_input': 'geometry', 'node_output': 'geometry'},
                        {'output_socket': bsocket,      'node_input': sock_index, 'node_output': sock_index},
                        ]
                    
                    self.insert_node(capt_node, cut_links)
                    
                    # The capture node containts now the new geometry output
                    
                    out_geometry = capt_node.geometry.bsocket
                    
                # Debug
                #diffs = context.changes_in_tree(self.btree, fprint)
                #print("Differences in tree")
                #for k, v in diffs.items():
                #    print(k)
                #    for line in v:
                #        print("   ... ", line)
                #print()
                
                
            # OLD VERSION 

            else:
            
                geo_links  = attr_node.owning_bsocket.links
                
                # Attribute
                
                attr_links_s    = []
                output_indices  = []
                for index, bsocket in enumerate(attr_node.bnode.outputs):
                    links = bsocket.links
                    if links:
                        attr_links_s.append(links)
                        output_indices.append(index)
                        
                if len(attr_links_s) == 0:
                    raise Exception("Algo error !")
    
                elif len(attr_links_s) > 1:
                    
                    frame = self.btree.nodes.new('NodeFrame')
                    frame.label = "Attribute error"
                    for nd in fed_nodes:
                        nd.bnode.parent = frame
                        nd.node_color = "cyan"
                        
                    for nd in end_nodes:
                        nd.bnode.parent = frame
                        nd.node_color = "blue"
                        
                    for nd in geometries:
                        nd.parent = frame
                        nd.node_color = "orange"
                        
                    attr_node.parent = frame
                    attr_node.node_color = "red"
                    
                    ok = False
                    for bnode in self.btree.nodes:
                        for bsock in bnode.outputs:
                            if bsock == attr_node.owning_bsocket:
                                self.get_bnode_wrapper(bnode).node_color = "red"
                                ok = True
                                break
                        if ok:
                            break
                    
                    print('-'*30)
                    for i, attr_links in enumerate(attr_links_s):
                        print(f" links {i}: index {output_indices[i]}")
                        for attr_link in attr_links:
                            node0 = self.get_bnode_wrapper(attr_link.from_node)
                            node1 = self.get_bnode_wrapper(attr_link.to_node)
                            print(f"   - {node0}.{attr_link.from_socket.name} --> {node1}.{attr_link.to_socket.name}")
                            node0.parent = frame
                            node1.parent = frame
                            
                    print("\nNode forwards")
                    for node in fed_nodes:
                        print(f"   - {node}")
                        
                    print("\nEnd of forward path")
                    for node in end_nodes:
                        print(f"   - {node}")
    
                    print("\nFeeding geometries")
                    for node in geometries:
                        print(f"   > {node}")
                    print()
                    
                    self.arrange()
                    
                    #### DEBUG
                    DEBUG = False 
                    if DEBUG:
                        attr_links   = attr_links_s[0]
                        output_index = output_indices[0]
                    else:
                        raise Exception(f"\nError when inserting a capture node. The attribute node '{attr_node}' has several output sockets which are connected.")
                        
                else:
                    attr_links   = attr_links_s[0]
                    output_index = output_indices[0]
                    
                    
                # ----- Capture node creation in the proper frame
                
                if False:
                    data_type = DataSocket.SOCKET_IDS[attr_node.bnode.outputs[output_index].bl_idname][2]
                    
                    capt_node = Geometry(attr_node.owning_bsocket).capture_attribute(value=attr_node.outputs[output_index], data_type=data_type, domain=attr_node.domain)
                    capt_node.bnode.parent = attr_node.bnode.parent
                else:
                    capt_node = Geometry(attr_node.owning_bsocket).capture_attribute(value=attr_node.outputs[output_index], domain=attr_node.domain).node
                    capt_node.bnode.parent = attr_node.bnode.parent
                    
                # ----- Some colors to track the process
                    
                if track_nodes:
                    for nd in geometries:
                        nd.node_color = "light yellow"
    
                    attr_node.node_color = "light yellow"
                    capt_node.node_color = "olive"
                
                # ----- Links rerouting
                
                # Geometry
                
                for link in geo_links:
                    to_socket = link.to_socket
                    self.btree.links.remove(link)
                    self.btree.links.new(capt_node.bnode.outputs[0], to_socket)
                    
                # Attribute
                
                for index, bsocket in enumerate(capt_node.bnode.outputs):
                    if index > 0 and bsocket.enabled:
                        out_bsocket = bsocket
                        break
                
                for link in attr_links:
                    to_socket = link.to_socket
                    self.btree.links.remove(link)
                    self.btree.links.new(out_bsocket, to_socket)
                        
     
    # ---------------------------------------------------------------------------
    # Get the parameter previously changed in a node
    
    def prev_node(self, index):
        """ Utility which prints the configuration of a node in the console.
        
        :param index: The unique id of the node to print
        :type index: int
        
        When a node is tweaked to obtain the expected result, the changes will be lost
        next time the script will be run. By calling `prev_node` the parameters are printed
        in the console and can be copied/pasted.
    
        """
        onode = self.previous.get(index)
        if onode is None:
            print(f"No previous node with index {index}")
        else:
            print(f"Previous node {onode.name}:\n{onode.args}\n")
    
    # ----------------------------------------------------------------------------------------------------
    # Arrange the nodes
    
    def arrange(self):
        """ Arrange the created nodes in the tree background for more lisibility
        """ 
        arrange(self.btree.name)    

    # ----------------------------------------------------------------------------------------------------
    # Close the tree
    #
    # Called by __exit__
    
    def close(self):
        """ Call to indicate that the tree is completed and that it can be finalized
        
        Three actions are performed:
            
        - Insertion of "Capture Attribute" nodes for attributes which require it,
          see :func:`check_attributes`.
        - Insert group input nodes in frame when ok_capture_inputs is set to True
        - Nodes arrangement, see :func:`arrange`.   
                                           
        """
        
        # ----- Capture attributes
        
        if self.capture_attributes:
            self.check_attributes()
            
        # ----- Capture inputs into the frames
        
        frames = [frame for frame in self.nodes if frame.bnode.bl_idname == 'NodeFrame']
        for frame in frames:
            if frame.ok_capture_inputs:
                frame.capture_inputs()
        
        # ----- Arrange
            
        self.arrange()
        
        print(f"Geonodes: tree '{self.btree.name}' built with {len(self.nodes)} nodes and {len(self.btree.links)} links.")


        
    
    
        