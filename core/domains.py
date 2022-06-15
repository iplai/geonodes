#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:20:40 2022

@author: alain
"""

from geonodes.core.node import Socket
from geonodes.nodes.nodes import create_node

import bpy

import logging
logger = logging.getLogger('geonodes')


# =============================================================================================================================
# Root class for domains: PointDomain, FaceDomain, EdgeDomain, CornerDomain, CurveDomain and Instance
#    
# Fields are properties of domains.
#   
# Initialization is made in method init_socket called by initializer Socket.__init__
#
# Domains classes
# ---------------
#
# Domain classes are implemented as properties of geometries:
#     - Mesh owns `point`, `edge`, `face` and `corner` properties (`vertex` and `face_corner`
#       can be used rather than `point` and `corner`)
#     - Curve owns `point` and `spline` (`control_point` can be used rather than `point`)
#     - Points owns `point`
#     - Instances has no domain properties, fields are direct properties of this class
#
# To get the index of a point, use the syntax:
#
# ```python
# position = mesh.point.position
# ```
#
# Thanks to this syntax, you always know which field you want.
#
# ```python
# # mesh, curve and instances are initialized respectively as Mesh, Curve ans Instances
#
# mesh.point.position  # position of the vertices
# mesg.vertex.position # same
# mesh.face.position   # position of the faces
# mesh.face.area       # faces area
# curve.point.position # location of the curve control_points
# instances.index      # Indices of the individual instances
# instances.position   # Location of the instances
# ```
#

class Domain(Socket):
        
    def init_socket(self):
        self.fields = {}
        
    def create_field_node(self, bl_idname, **kwargs):
        """ > Create a **geonodes** from a bl_idname
        
        If kwargs is an empty dict, the node is put in cache in the _fields_ dict,
        otherwise it is returned directly.
        
        Attributes
        ----------
            - bl_idname : str
                A valid node bl_idname
            - kwargs : dict
                Arguments to pass to initialize the node
                
        Returns
        -------
            Node, the created node
        """
        
        cache = len(kwargs) == 0
        
        node = self.fields.get(bl_idname) if cache else None

        if node is None:
            node = create_node(bl_idname, **kwargs)
            node.as_attribute(self.bsocket, domain=self.domain)
            if cache:
                self.fields[bl_idname] = node
        return node
    
    # ---------------------------------------------------------------------------
    # Input menu
        
    @property
    def ID(self):
        """ <field GeometryNodeInputID>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.create_field_node('GeometryNodeInputID').ID
        
    @property
    def index(self):
        """ <field GeometryNodeInputIndex>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.create_field_node('GeometryNodeInputIndex').index

    @property
    def normal(self):
        """ <field GeometryNodeInputNormal>
        
        Property
        
        Returns
        -------
            Vector
        """
        return self.create_field_node('GeometryNodeInputNormal').normal
    
    @property
    def position(self):
        """ <field GeometryNodeInputPosition>
        
        Property
        
        Returns
        -------
            Vector
        """
        return self.create_field_node('GeometryNodeInputPosition').position
    
    @property
    def radius(self):
        """ <field GeometryNodeInputRadius>
        
        Property
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputRadius').radius
    
    def named_attribute(self, name=None, data_type='FLOAT'):
        """ <field GeometryNodeInputNamedAttribute>
        
        This method is called by the following methods:
            - [named_float](#named_float)
            - [named_integer](#named_integer)
            - [named_vector](#named_vector)
            - [named_color](#named_color)
            - [named_boolean](#named_boolean)
        
        Returns
        -------
            Linked to data_type
        """
        return self.create_field_node('GeometryNodeInputNamedAttribute', name=name).attribute
    
    def named_float(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'FLOAT'
                               
        Returns
        -------
            Float
        """
        return self.named_attribute(name, data_type='FLOAT')
    
    def named_integer(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'INT'
        """
        return self.named_attribute(name, data_type='INT')
    
    def named_vector(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'FLOAT_VECTOR'
                               
        Returns
        -------
            Vector
        """
        return self.named_attribute(name, data_type='FLOAT_VECTOR')
    
    def named_color(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'FLOAT_COLOR'
                               
        Returns
        -------
            Color
        """
        return self.named_attribute(name, data_type='FLOAT_COLOR')
    
    def named_boolean(self, name):
        """ <field GeometryNodeInputNamedAttribute>
        
        Call [named_attribute](#named_attribute) with data_type = 'BOOLEAN'
                               
        Returns
        -------
            Boolean
        """
        return self.named_attribute(name, data_type='BOOLEAN')
        

# ---------------------------------------------------------------------------
# > Field domain POINT
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh, Curve, Points

class PointDomain(Domain):
    
    def init_socket(self):
        super().init_socket()
        self.domain = 'POINT'

    @property
    def neighbors(self):
        """ <field GeometryNodeInputMeshVertexNeighbors>
        
        Property

        Individual sockets can be accessed via propertyes:
            - [neighbors_vertices](#neighbors_vertices)
            - [neighbors_faces](#neighbors_faces)
        
        Returns
        -------
            Node with two sockets:
                - vertex_count
                - face_count
        """
        return self.create_field_node('GeometryNodeInputMeshVertexNeighbors')
    
    @property
    def neighbors_vertices(self):
        """ <field GeometryNodeInputMeshVertexNeighbors>
        
        Property
        
        Return the socket **vertex_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.vertex_count
    
    @property
    def neighbors_faces(self):
        """ <field GeometryNodeInputMeshVertexNeighbors>
        
        Property
        
        Return the socket **face_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.face_count
    
# ---------------------------------------------------------------------------
# > Field domain FACE
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh

class FaceDomain(Domain):

    def init_socket(self):
        super().init_socket()
        self.domain = 'FACE'
        
    @property
    def area(self):
        """ <field GeometryNodeInputMeshFaceArea>
        
        Property
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputMeshFaceArea').area
    
    @property
    def neighbors(self):
        """ <field GeometryNodeInputMeshFaceNeighbors>
        
        Property

        Individual sockets can be accessed via propertyes:
            - [neighbors_vertices](#neighbors_vertices)
            - [neighbors_faces](#neighbors_faces)
        
        Returns
        -------
            Node with two sockets:
                - vertex_count
                - face_count
        """
        return self.create_field_node('GeometryNodeInputMeshFaceNeighbors')
    
    @property
    def neighbors_vertices(self):
        """ <field GeometryNodeInputMeshFaceNeighbors>
        
        Property
        
        Return the socket **vertex_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.vertex_count
    
    @property
    def neighbors_faces(self):
        """ <field GeometryNodeInputMeshFaceNeighbors>
        
        Property
        
        Return the socket **face_count** of property [neighbors](#neighbors)
        
        Returns
        -------
            Integer
        """
        return self.neighbors.face_count
    
    @property
    def is_shade_smooth(self):
        """ <field GeometryNodeInputShadeSmooth>
        
        Property
        
        Returns
        -------
            Float
        """
        return self.create_field_node('GeometryNodeInputShadeSmooth').smooth
    
    @property
    def island(self):
        """ <field GeometryNodeInputMeshIsland>
        
        Property

        Individual sockets can be accessed via propertyes:
            - [neighbors_vertices](#neighbors_vertices)
            - [neighbors_faces](#neighbors_faces)
        
        Returns
        -------
            Node with two sockets:
                - vertex_count
                - face_count
        """
        return self.create_field_node('GeometryNodeInputMeshIsland')
    
    @property
    def island_vertices(self):
        """ <field GeometryNodeInputMeshIsland>
        
        Property
        
        Return the socket **vertex_count** of property [island](#island)
        
        Returns
        -------
            Integer
        """
        return self.island.vertex_count
    
    @property
    def island_faces(self):
        """ <field GeometryNodeInputMeshIsland>
        
        Property
        
        Return the socket **face_count** of property [island](#island)
        
        Returns
        -------
            Integer
        """
        return self.island.face_count

    @property
    def material_index(self):
        """ <field GeometryNodeInputMaterialIndex>
        
        Property
        
        Returns
        -------
            Integer
        """
        return self.create_field_node('GeometryNodeInputMaterialIndex').material_index
    
    def material_selection(self, material=None):
        """ <field GeometryNodeMaterialSelection>
        
        Method
        
        Arguments
        ---------
            - material : Material
        
        Returns
        -------
            Boolean
        """
        return self.create_field_node('GeometryNodeMaterialSelection', material=material).selection
    
    def face_is_planar(self, threshold=None):
        """ <field GeometryNodeInputMeshFaceIsPlanar>
        
        Method
        
        Arguments
        ---------
            - threshold : Float
        
        Returns
        -------
            Boolean
        """
        return self.create_field_node('GeometryNodeInputMeshFaceIsPlanar', threshold=threshold).planar
    
    
# ---------------------------------------------------------------------------
# > Field domain FACE
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh
        
        
class EdgeDomain(Domain):
    
    def init_socket(self):
        super().init_socket()
        self.domain = 'EDGE'
        
    @property
    def angle(self):
        return self.create_field_node('GeometryNodeInputMeshEdgeAngle').signed_angle
    
    @property
    def unsigned_angle(self):
        return self.create_field_node('GeometryNodeInputMeshEdgeAngle').unsigned_angle
    
    @property
    def neighbors(self):
        return self.create_field_node('GeometryNodeInputMeshEdgeNeighbors').face_count
    
    @property
    def vertices(self):
        return self.create_field_node('GeometryNodeInputMeshEdgeVertices')
    
    @property
    def vertices_index_1(self):
        return self.vertices.vertex_index_1
    
    @property
    def vertices_index_2(self):
        return self.vertices.vertex_index_2
    
    @property
    def vertices_position_1(self):
        return self.vertices.position_1
    
    @property
    def vertices_position_2(self):
        return self.vertices.position_2
    
    @property
    def island(self):
        return self.create_field_node('GeometryNodeInputMeshIsland')
    
    @property
    def island_vertices(self):
        return self.island.vertex_count
    
    @property
    def island_faces(self):
        return self.island.face_count
    
# ---------------------------------------------------------------------------
# > Field domain CORNER
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Mesh
        

class CornerDomain(Domain):
    
    def init_socket(self):
        super().init_socket()
        self.domain = 'CORNER'
        
# ---------------------------------------------------------------------------
# > Field domain CURVE
#
# Inherits from [Domain](/docs/core/domain.MD)
#
# A property of Spline and Curve

class CurveDomain(Domain):
    
    def init_socket(self):
        super().init_socket()
        self.domain = 'CURVE'
        
    def handle_positions(self, relative=None):
        return self.create_field_node('GeometryNodeInputCurveHandlePositions', relative=relative)
    
    def handle_positions_left(self, relative=None):
        return self.handle_positions(relative=relative).left
    
    def handle_positions_right(self, relative=None):
        return self.handle_positions(relative=relative).right
    
    @property
    def tangent(self):
        return self.create_field_node('GeometryNodeInputTangent').tangent
    
    @property
    def tilt(self):
        return self.create_field_node('GeometryNodeInputCurveTilt').tilt
    
    def endpoint_selection(self, start_size=None, end_size=None):
        return self.create_field_node('GeometryNodeCurveEndpointSelection', start_size=start_size, end_size=end_size).selection
    
    def handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        return self.create_field_node('GeometryNodeCurveHandleTypeSelection', handle_type=handle_type, mode=mode).selection
    
    def left_handle_selection(self, handle_type='AUTO'):
        return self.handle_type_selection(handle_type=handle_type, mode='LEFT')

    def right_handle_selection(self, handle_type='AUTO'):
        return self.handle_type_selection(handle_type=handle_type, mode='RIGHT')
    
    @property
    def left_handle_free(self):
        return self.left_handle_selection(handle_type='FREE')
    
    @property
    def left_handle_auto(self):
        return self.left_handle_selection(handle_type='AUTO')
    
    @property
    def left_handle_vector(self):
        return self.left_handle_selection(handle_type='VECTOR')
    
    @property
    def left_handle_align(self):
        return self.left_handle_selection(handle_type='ALIGN')
    
    @property
    def right_handle_free(self):
        return self.left_handle_selection(handle_type='FREE')
    
    @property
    def right_handle_auto(self):
        return self.left_handle_selection(handle_type='AUTO')
    
    @property
    def right_handle_vector(self):
        return self.left_handle_selection(handle_type='VECTOR')
    
    @property
    def right_handle_align(self):
        return self.left_handle_selection(handle_type='ALIGN')
    
    @property
    def cyclic(self):
        return self.create_field_node('GeometryNodeInputSplineCyclic').cyclic
    
    @property
    def length_point_count(self):
        return self.create_field_node('GeometryNodeSplineLength')
    
    @property
    def length(self):
        return self.length_point_count.length
    
    @property
    def point_count(self):
        return self.length_point_count.point_count
    
    @property
    def parameter(self):
        return self.create_field_node('GeometryNodeSplineParameter')
    
    @property
    def factor(self):
        return self.parameter.factor
    
    @property
    def parameter_length(self):
        return self.parameter.length
    
    @property
    def parameter_index(self):
        return self.parameter.index
    
    @property
    def resolution(self):
        return self.create_field_node('GeometryNodeInputSplineResolution').resolution
        
