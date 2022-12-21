# Node Edges of Corner

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeEdgesOfCorner`

```python
from geonodes import nodes

node = nodes.EdgesOfCorner(corner_index=None)
```

#### Input socket arguments:

- corner_index: Integer

#### Output sockets:

- **next_edge_index** : Integer
- **previous_edge_index** : Integer
