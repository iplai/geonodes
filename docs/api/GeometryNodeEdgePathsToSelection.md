# Node Edge Paths to Selection

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_selection.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeEdgePathsToSelection`

```python
from geonodes import nodes

node = nodes.EdgePathsToSelection(start_vertices=None, next_vertex_index=None)
```

#### Input socket arguments:

- start_vertices: Boolean
- next_vertex_index: Integer

#### Output sockets:

- **selection** : Boolean
