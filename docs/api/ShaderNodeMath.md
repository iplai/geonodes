# Node Math

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
- geonodes name: `WNode`
- bl_idname: `ShaderNodeMath`

```python
from geonodes import nodes

node = nodes.Math(value0=None, value1=None, value2=None, operation='ADD', use_clamp=False)
```

#### Input socket arguments:

- value0: Float
- value1: Float
- value2: Float

#### Node parameter arguments:

- operation (str): Node parameter, default = 'ADD' in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')
- use_clamp (bool): Node parameter, default = False

#### Output sockets:

- **value** : Float
