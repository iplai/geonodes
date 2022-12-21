# Node Separate XYZ

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
- geonodes name: `WNode`
- bl_idname: `ShaderNodeSeparateXYZ`

```python
from geonodes import nodes

node = nodes.SeparateXyz(vector=None)
```

#### Input socket arguments:

- vector: Vector

#### Output sockets:

- **x** : Float
- **y** : Float
- **z** : Float
