# Node Set Point Radius

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSetPointRadius`

```python
from geonodes import nodes

node = nodes.SetPointRadius(points=None, selection=None, radius=None)
```

#### Input socket arguments:

- points: Points
- selection: Boolean
- radius: Float

#### Output sockets:

- **points** : Points
