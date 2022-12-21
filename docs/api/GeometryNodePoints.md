# Node Points

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodePoints`

```python
from geonodes import nodes

node = nodes.Points(count=None, position=None, radius=None)
```

#### Input socket arguments:

- count: Integer
- position: Vector
- radius: Float

#### Output sockets:

- **geometry** : Geometry
