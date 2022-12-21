# Node Rotate Instances

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeRotateInstances`

```python
from geonodes import nodes

node = nodes.RotateInstances(instances=None, selection=None, rotation=None, pivot_point=None, local_space=None)
```

#### Input socket arguments:

- instances: Instances
- selection: Boolean
- rotation: Vector
- pivot_point: Vector
- local_space: Boolean

#### Output sockets:

- **instances** : Instances
