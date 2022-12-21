# Node Realize Instances

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeRealizeInstances`

```python
from geonodes import nodes

node = nodes.RealizeInstances(geometry=None, legacy_behavior=False)
```

#### Input socket arguments:

- geometry: Geometry

#### Node parameter arguments:

- legacy_behavior (bool): Node parameter, default = False

#### Output sockets:

- **geometry** : Geometry
