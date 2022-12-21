# Node Group Output

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/r.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.NodeGroupOutput.html)
- geonodes name: `WNode`
- bl_idname: `NodeGroupOutput`

```python
from geonodes import nodes

node = nodes.GroupOutput(geometry=None, is_active_output=True)
```

#### Input socket arguments:

- geometry: Geometry

#### Node parameter arguments:

- is_active_output (bool): Node parameter, default = True
