# Node Combine XYZ

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/combine_xyz.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)
- geonodes name: `WNode`
- bl_idname: `ShaderNodeCombineXYZ`

```python
from geonodes import nodes

node = nodes.CombineXyz(x=None, y=None, z=None)
```

#### Input socket arguments:

- x: Float
- y: Float
- z: Float

#### Output sockets:

- **vector** : Vector
