Class Float

## Properties

### bl_idname

         Shortcut for `self.bsocket.bl_idname`
        


### bnode

         Shortcut for `self.bsocket.node`
        


### color_ramp

         Node ColorRamp.

        Node reference [ColorRamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html)
        Developer reference [ShaderNodeValToRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)

        Returns:
            node with sockets ['color', 'alpha']
        


### is_multi_input

         Shortcut for `self.bsocket.is_multi_output`
        


### is_output

         Shortcut for `self.bsocket.is_output`
        


### links

         Shortcut for `self.bsocket.links`
        


### name

         Shortcut for `self.bsocket.name`
        


### node_chain_label

         Shortcut for *self.node.chain_label*
        


### socket_index

         Return the index of the socket within the list of node sockets.
        
        Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
        *node.outputs*.
        



## Class and static methods

### Angle

```python
@classmethod
def Angle(cls, value=0., name="Angle", min_value = None, max_value = None, description ="")
```

         Create an Angle input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            min_value: Minimum value
            max_value: Maximum value
            description: User tip
            
        Returns:
            Float: The Float data socket
        



### Distance

```python
@classmethod
def Distance(cls, value=0., name="Distance", min_value = None, max_value = None, description ="")
```

         Create a Distance input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            min_value: Minimum value
            max_value: Maximum value
            description: User tip
            
        Returns:
            Float: The Float data socket
        



### Factor

```python
@classmethod
def Factor(cls, value=0., name="Factor", min_value = 0., max_value = 1., description ="")
```

         Create a Factor input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            min_value: Minimum value
            max_value: Maximum value
            description: User tip
            
        Returns:
            Float: The Float data socket
        



### Frame

```python
@classmethod
def Frame(cls)
```

         Node SceneTime.

        Node reference [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html)
        Developer reference [GeometryNodeInputSceneTime](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)

        Returns:
            socket `frame`
        


### Input

```python
@classmethod
def Input(cls, value = 0., name = "Float", min_value = None, max_value = None, description ="")
```

         Create a Float input socket in the Group Input Node
        
        Args:
            value: The default value
            name: The socket name
            min_value: Minimum value
            max_value: Maximum value
            description: User tip
            
        Returns:
            Float: The Float data socket
        


### Seconds

```python
@classmethod
def Seconds(cls)
```

         Node SceneTime.

        Node reference [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html)
        Developer reference [GeometryNodeInputSceneTime](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)

        Returns:
            socket `seconds`
        


### Value

```python
@classmethod
def Value(cls)
```

         Node Value.

        Node reference [Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/value.html)
        Developer reference [ShaderNodeValue](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html)

        Returns:
            socket `value`
        


### get_bl_idname

```python
@staticmethod
def get_bl_idname(class_name)
```

         Get the node socket bl_idname name from the Socket class
        
        :param class_name: The class name
        :type class_name: str
        :return: The bl_idname associated to this class name
        :rtype: str
        
        Used to create a new group input socket. Called in `DataClass.Input` method to determine
        which socket type must be created.
        
        Note that here the class_name argument accepts additional values which correspond to *sub classes*:
            
        .. list-table:: 
           :widths: 20 40
           :header-rows: 0
        
           * - Unsigned
             - Integer sub class (NodeSocketIntUnsigned)
           * - Factor
             - Float sub class (NodeSocketFloatFactor)
           * - Angle
             - Float sub class  (NodeSocketFloatAngle)
           * - Distance
             - Float sub class (NodeSocketFloatDistance)
           * - Rotation
             - Vector sub class (NodeSocketVectorEuler)
           * - xyz
             - Vector sub class (NodeSocketVectorXYZ)
           * - Translation
             - Vector sub class (NodeSocketVectorTranslation)
          
        These additional values allow to enter angle, distance, factor... as group input values.
        



### get_class_name

```python
@staticmethod
def get_class_name(socket, with_sub_class = False)
```

         Get the DataSocket class name corresponding to the socket type and name.
        
        :param socket: The socket to determine the class of
        :param with_sub_class: Return the sub class if True
        :typ socket: bpy.types.NodeSocket, Socket
        :type with_sub_class: bool
        :return: The name of the class associated to the bl_idname of the socket
        :rtype: str
        
        .. list-table:: Correspondance table
           :widths: 30 20 20
           :header-rows: 1
           
           * - NodeSocket
             - class name
             - sub class name
           * - NodeSocketBool 
             - 'Boolean'
             - 
           * - NodeSocketInt 
             - 'Integer'
             - 
           * - NodeSocketIntUnsigned 
             - 'Integer'
             - 'Unsigned'
           * - NodeSocketFloat 
             - 'Float' 
             - 
           * - NodeSocketFloatFactor 
             - 'Float'
             - 'Factor'
           * - NodeSocketFloatAngle  
             - 'Float'
             - 'Angle'
           * - NodeSocketFloatDistance 
             - 'Float'
             - 'Distance'
           * - NodeSocketVector 
             - 'Vector'
             - 
           * - NodeSocketVectorEuler 
             - 'Vector'
             - 'Rotation'
           * - NodeSocketVectorXYZ 
             - 'Vector'
             - 'xyz'
           * - NodeSocketVectorTranslation 
             - 'Vector'
             - 'Translation'
           * - NodeSocketColor 
             - 'Color'
             - 
           * - NodeSocketString' 
             - 'String'
             - 
           * - NodeSocketCollection 
             - 'Collection'
             - 
           * - NodeSocketImage 
             - 'Image'
             - 
           * - NodeSocketMaterial 
             - 'Material'
             - 
           * - NodeSocketObject 
             - 'Object'
             - 
           * - NodeSocketTexture 
             - 'Texture'
             - 
           * - NodeSocketGeometry
             - 'Geometry'
             - 
          
          
        If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
        the name is chosen as the class name.
        


### gives_bsocket

```python
@staticmethod
def gives_bsocket(value)
```

         Test if the argument provides a valid output socket.
        
        :param value: The value to test
        :type value: any
        :return: True if *value* is or wraps a socket
        :rtype: bool
        
        Returns True if value is:
            
        - A Blender Geometry Node Socket
        - An instance of Socket        
        



### is_socket

```python
@staticmethod
def is_socket(value)
```

         An alternative to isinstance(value, Socket)

        :param value: The value to test
        :type value: any
        :return: True if *value* is an instance of Socket
        :rtype: bool
        


### is_vector

```python
@staticmethod
def is_vector(value)
```

         Determine is the parameter is a vector.

        :param value: The value to test
        :type value: any
        :return: True if *value* is an instance of Socket
        :rtype: bool
        



### value_data_type

```python
@staticmethod
def value_data_type(value, default='FLOAT', color_domain='FLOAT_COLOR')
```

         Returns the domain to which the socket belongs
        
        :param value: The socket
        :type value: any
        :return: data type in ['BOOLEAN', 'INT', 'FLOAT', 'FLOAT_VECTOR', 'FLOAT_COLOR']
        :rtype: str
        
        .. list-table:: Correspondance table
           :widths: 30 20
           :header-rows: 1
        
           * - Socket bl_idname
             - Domain code
           * - NodeSocketBool
             - 'BOOLEAN'
           * - NodeSocketInt               
             - 'INT'
           * - NodeSocketIntUnsigned       
             - 'INT'
           * - NodeSocketFloat            
             - 'FLOAT'
           * - NodeSocketFloatFactor       
             - 'FLOAT'
           * - NodeSocketFloatAngle        
             - 'FLOAT'
           * - NodeSocketFloatDistance     
             - 'FLOAT'         
           * - NodeSocketVector            
             - 'FLOAT_VECTOR'
           * - NodeSocketVectorEuler       
             - 'FLOAT_VECTOR'
           * - NodeSocketVectorXYZ         
             - 'FLOAT_VECTOR'
           * - NodeSocketVectorTranslation
             - 'FLOAT_VECTOR'
           * - NodeSocketColor      
             - 'FLOAT_COLOR'
           * - NodeSocketString           
             - 'FLOAT_COLOR'
        
        



## Methods

### abs

```python
def abs(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### absolute

```python
def absolute(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### add

```python
def add(self, value=None, node_label = None, node_color = None)
```

         Add two values.
        
            Args:
                value: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value is a Vector or a Color, VectorMath node is used rather than Math.
        



### arccos

```python
def arccos(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### arccosine

```python
def arccosine(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### arcsin

```python
def arcsin(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### arcsine

```python
def arcsine(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### arctan

```python
def arctan(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### arctan2

```python
def arctan2(self, value1=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value1: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### arctangent

```python
def arctangent(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### ceiling

```python
def ceiling(self)
```

         Node FloatToInteger.

        Node reference [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html)
        Developer reference [FunctionNodeFloatToInt](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

        Returns:
            socket `integer`
        


### clamp

```python
def clamp(self, min=None, max=None, clamp_type='MINMAX')
```

         Node Clamp.

        Node reference [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)
        Developer reference [ShaderNodeClamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

        Args:
            min: Float
            max: Float
            clamp_type (str): 'MINMAX' in [MINMAX, RANGE]

        Returns:
            socket `result`
        


### clamp_min_max

```python
def clamp_min_max(self, min=None, max=None)
```

         Node Clamp.

        Node reference [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)
        Developer reference [ShaderNodeClamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

        Args:
            min: Float
            max: Float

        Returns:
            socket `result`
        


### clamp_range

```python
def clamp_range(self, min=None, max=None)
```

         Node Clamp.

        Node reference [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)
        Developer reference [ShaderNodeClamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

        Args:
            min: Float
            max: Float

        Returns:
            socket `result`
        


### compare

```python
def compare(self, b=None, epsilon=None, operation='GREATER_THAN')
```

         Node Compare.

        Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
        Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        Args:
            b: ['Float', 'Integer', 'Vector', 'Color', 'String']
            epsilon: Float
            operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

        Returns:
            socket `result`
        


### connected_sockets

```python
def connected_sockets(self)
```

         Returns the list of Socket instances linked to this socket.
        



### cos

```python
def cos(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### cosh

```python
def cosh(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### cosine

```python
def cosine(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### divide

```python
def divide(self, value=None, node_label = None, node_color = None)
```

         Divide two values.
        
            Args:
                value: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value is a Vector or a Color, VectorMath node is used rather than Math.
        



### equal

```python
def equal(self, b=None, epsilon=None)
```

         Node Compare.

        Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
        Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        Args:
            b: ['Float', 'Integer', 'Vector', 'Color', 'String']
            epsilon: Float

        Returns:
            socket `result`
        


### exp

```python
def exp(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### exponent

```python
def exponent(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### fact

```python
def fact(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### float_curve

```python
def float_curve(self, factor=None)
```

         Node FloatCurve.

        Node reference [Float Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_curve.html)
        Developer reference [ShaderNodeFloatCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)

        Args:
            factor: Float

        Returns:
            socket `value`
        


### floor

```python
def floor(self)
```

         Node FloatToInteger.

        Node reference [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html)
        Developer reference [FunctionNodeFloatToInt](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

        Returns:
            socket `integer`
        


### fraction

```python
def fraction(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### get_blender_socket

```python
def get_blender_socket(self)
```

         Returns the property bsocket.
        
        :return: self.bsocket
        :rtype: bpy.types.NodeSocket
        



### greater_equal

```python
def greater_equal(self, b=None)
```

         Node Compare.

        Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
        Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        Args:
            b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        Returns:
            socket `result`
        


### greater_than

```python
def greater_than(self, b=None)
```

         Node Compare.

        Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
        Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        Args:
            b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        Returns:
            socket `result`
        


### init_domains

```python
def init_domains(self)
```

         Initialize the geometry domains
        
        To be overloaded by sub classes.        
        


### init_socket

```python
def init_socket(self)
```

         Complementary init
        
        Called at the end of initialization for further operations.
        


### inverse_sqrt

```python
def inverse_sqrt(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### less_equal

```python
def less_equal(self, b=None)
```

         Node Compare.

        Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
        Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        Args:
            b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        Returns:
            socket `result`
        


### less_than

```python
def less_than(self, b=None)
```

         Node Compare.

        Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
        Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        Args:
            b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        Returns:
            socket `result`
        


### log

```python
def log(self, base=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            base: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### logarithm

```python
def logarithm(self, base=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            base: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### map_range

```python
def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR')
```

         Node MapRange.

        Node reference [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
        Developer reference [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        Args:
            from_min: ['Float', 'Vector']
            from_max: ['Float', 'Vector']
            to_min: ['Float', 'Vector']
            to_max: ['Float', 'Vector']
            steps: ['Float', 'Vector']
            clamp (bool): True
            interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]

        Returns:
            socket `result`
        


### map_range_linear

```python
def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```

         Node MapRange.

        Node reference [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
        Developer reference [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        Args:
            from_min: ['Float', 'Vector']
            from_max: ['Float', 'Vector']
            to_min: ['Float', 'Vector']
            to_max: ['Float', 'Vector']
            clamp (bool): True

        Returns:
            socket `result`
        


### map_range_smooth

```python
def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```

         Node MapRange.

        Node reference [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
        Developer reference [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        Args:
            from_min: ['Float', 'Vector']
            from_max: ['Float', 'Vector']
            to_min: ['Float', 'Vector']
            to_max: ['Float', 'Vector']
            clamp (bool): True

        Returns:
            socket `result`
        


### map_range_smoother

```python
def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```

         Node MapRange.

        Node reference [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
        Developer reference [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        Args:
            from_min: ['Float', 'Vector']
            from_max: ['Float', 'Vector']
            to_min: ['Float', 'Vector']
            to_max: ['Float', 'Vector']
            clamp (bool): True

        Returns:
            socket `result`
        


### map_range_stepped

```python
def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True)
```

         Node MapRange.

        Node reference [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
        Developer reference [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        Args:
            from_min: ['Float', 'Vector']
            from_max: ['Float', 'Vector']
            to_min: ['Float', 'Vector']
            to_max: ['Float', 'Vector']
            steps: ['Float', 'Vector']
            clamp (bool): True

        Returns:
            socket `result`
        


### math_ceil

```python
def math_ceil(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### math_compare

```python
def math_compare(self, value=None, epsilon=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            epsilon: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### math_floor

```python
def math_floor(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### math_greater_than

```python
def math_greater_than(self, threshold=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            threshold: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### math_less_than

```python
def math_less_than(self, threshold=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            threshold: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### math_round

```python
def math_round(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### math_trunc

```python
def math_trunc(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### math_truncate

```python
def math_truncate(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### max

```python
def max(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### maximum

```python
def maximum(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### min

```python
def min(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### minimum

```python
def minimum(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### mix

```python
def mix(self, factor=None, value=None, clamp_factor=True)
```

         Node Mix.

        Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
        Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        Args:
            factor: ['Float', 'Vector']
            value: ['Float', 'Vector', 'Color']
            clamp_factor (bool): True

        Returns:
            socket `result`
        


### modulo

```python
def modulo(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### mul_add

```python
def mul_add(self, multiplier=None, addend=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            multiplier: Float
            addend: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### multiply

```python
def multiply(self, value=None, node_label = None, node_color = None)
```

         Multiply two values.
        
            Args:
                value: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value is a Vector or a Color, VectorMath node is used rather than Math.
        



### multiply_add

```python
def multiply_add(self, multiplier=None, addend=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            multiplier: Float
            addend: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### not_equal

```python
def not_equal(self, b=None, epsilon=None)
```

         Node Compare.

        Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
        Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        Args:
            b: ['Float', 'Integer', 'Vector', 'Color', 'String']
            epsilon: Float

        Returns:
            socket `result`
        


### ping_pong

```python
def ping_pong(self, scale=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            scale: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### plug

```python
def plug(self, *values)
```

         Plug values in the socket (input sockets only)
        
        :param values: The output sockets. More than one values can be passed
            if the input socket is multi input.
        :type values: array of bpy.types.NodeSocket, Socket, values
        
        see :func:`plug_bsocket`
        


### pow

```python
def pow(self, exponent=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            exponent: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### power

```python
def power(self, exponent=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            exponent: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### reroute

```python
def reroute(self)
```

         Reroute all output links
        


### reset_properties

```python
def reset_properties(self)
```

         Reset the properties
        
        Properties such as components are cached.
        
        After a node is called, the wrapped socket changes and this makes the cache obsolete.
        After a change, the cache is erased.
        
        :example:
        
        .. code-block:: python
    
            class Vector(...):
                def __init__(self, ...):
                     ...
                     self.reset_properties()
                     ...
            
                 def reset_properties(self):
                     super().reset_properties()
                     self.separate_ = None      # Created by property self.seperate() with node SeparateXyz

        
        



### round

```python
def round(self)
```

         Node FloatToInteger.

        Node reference [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html)
        Developer reference [FunctionNodeFloatToInt](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

        Returns:
            socket `integer`
        


### sign

```python
def sign(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### sin

```python
def sin(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### sine

```python
def sine(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### sinh

```python
def sinh(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### smooth_maximum

```python
def smooth_maximum(self, value=None, distance=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            distance: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### smooth_minimum

```python
def smooth_minimum(self, value=None, distance=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            distance: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### snap

```python
def snap(self, increment=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            increment: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### sqrt

```python
def sqrt(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### stack

```python
def stack(self, node, socket_name=None)
```

         Change the wrapped socket
        
        :param node: The new node owning the output socket to wrap
        :type node: Node
        :return: self
        
        Methods are implemented in two modes:
        
        - Creation
        - Transformation
        
        In **creation mode**, the node is considered as creating new data. The result is a new instance of DataSocket.
        
        In **transformation mode**, the node is considered as transforming data which is kept in the result of the method.
        After the method returns, the calling DataSocket instance refers to a new Blender output socket.
        The stack method changes the socket the instance refers to and reinitialize properties
        
        .. code-block:: python

            # 1. Creation mode
            # 
            # to_mesh method creates a new mesh from a curve.
            # The curve instance refers to the same output node socket
            # We need to get the result of the method in a new variable
            
            new_mesh = curve.to_mesh(profile_curve=circle)
            
            # 2. Transformation mode
            #
            # set_shade_smooth method transforms the mesh.
            # After the call, the mesh instance refers to the output socket of the
            # newly created node "Set Shade Smooth". There is no need to get the result
            # of the method.
            
            mesh.set_shade_smooth()
            
            # Note that a transformation method returns self and so, the following line
            # is equivallent:
            
            mesh = mesh.set_shade_smooth()
        
        



### subtract

```python
def subtract(self, value=None, node_label = None, node_color = None)
```

         Subtract two values.
        
            Args:
                value: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            If value is a Vector or a Color, VectorMath node is used rather than Math.
        



### switch

```python
def switch(self, switch=None, true=None)
```

         Node Switch.

        Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
        Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        Args:
            switch: Boolean
            true: Float

        Returns:
            socket `output`
        


### tan

```python
def tan(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### tangent

```python
def tangent(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### tanh

```python
def tanh(self, value=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            value: Float
            clamp (bool): False

        Returns:
            socket `value`
        


### to_degrees

```python
def to_degrees(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### to_integer

```python
def to_integer(self, rounding_mode='ROUND')
```

         Node FloatToInteger.

        Node reference [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html)
        Developer reference [FunctionNodeFloatToInt](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

        Args:
            rounding_mode (str): 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]

        Returns:
            socket `integer`
        


### to_output

```python
def to_output(self, name=None)
```

         Plug the data socket to the group output
        
        :param name: The name to give to the modifier output
        :type name: str
        
        The socket is added to the outputs of the geometry nodes tree.
        
        .. Note:: To define a data socket as the result geometry of the tree, use ``tree.output_geometry = my_geometry``.
        
        


### to_radians

```python
def to_radians(self, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            clamp (bool): False

        Returns:
            socket `value`
        


### to_string

```python
def to_string(self, decimals=None)
```

         Node ValueToString.

        Node reference [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html)
        Developer reference [FunctionNodeValueToString](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)

        Args:
            decimals: Integer

        Returns:
            socket `string`
        


### truncate

```python
def truncate(self)
```

         Node FloatToInteger.

        Node reference [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html)
        Developer reference [FunctionNodeFloatToInt](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

        Returns:
            socket `integer`
        


### view

```python
def view(self, domain='AUTO', label=None, node_color=None)
```

         Link the data socket to the viewer
        
        If the data socket is a geometry (Curve, Mesh...) it is linked to the geometry input of the viewer.
        
        If it ias a value (Integer, Float,...) it is linked to the value socket and the viewer is configured
        accordingly.
        


### wrap

```python
def wrap(self, max=None, min=None, clamp=False)
```

         Node Math.

        Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
        Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        Args:
            max: Float
            min: Float
            clamp (bool): False

        Returns:
            socket `value`
        

