# Node Vertex of Corner

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/vertex_of_corner.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeVertexOfCorner`

```python
from geonodes import nodes

node = nodes.VertexOfCorner(corner_index=None)
```

#### Input socket arguments:

- corner_index: Integer

#### Output sockets:

- **vertex_index** : Integer
