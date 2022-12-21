# Node Rotate Euler

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
- geonodes name: `WNode`
- bl_idname: `FunctionNodeRotateEuler`

```python
from geonodes import nodes

node = nodes.RotateEuler(rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', type='EULER')
```

#### Input socket arguments:

- rotation: Vector
- rotate_by: Vector
- axis: Vector
- angle: Float

#### Node parameter arguments:

- space (str): Node parameter, default = 'OBJECT' in ('OBJECT', 'LOCAL')
- type (str): Node parameter, default = 'EULER' in ('AXIS_ANGLE', 'EULER')

#### Output sockets:

- **rotation** : Vector
