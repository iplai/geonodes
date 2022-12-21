# Node Merge by Distance

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMergeByDistance`

```python
from geonodes import nodes

node = nodes.MergeByDistance(geometry=None, selection=None, distance=None, mode='ALL')
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean
- distance: Float

#### Node parameter arguments:

- mode (str): Node parameter, default = 'ALL' in ('ALL', 'CONNECTED')

#### Output sockets:

- **geometry** : Geometry
