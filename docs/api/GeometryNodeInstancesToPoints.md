# Node Instances to Points

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeInstancesToPoints`

```python
from geonodes import nodes

node = nodes.InstancesToPoints(instances=None, selection=None, position=None, radius=None)
```

#### Input socket arguments:

- instances: Instances
- selection: Boolean
- position: Vector
- radius: Float

#### Output sockets:

- **points** : Points
