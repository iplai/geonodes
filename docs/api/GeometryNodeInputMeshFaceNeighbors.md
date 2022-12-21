# Node Face Neighbors

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeInputMeshFaceNeighbors`

```python
from geonodes import nodes

node = nodes.FaceNeighbors()
```

#### Output sockets:

- **vertex_count** : Integer
- **face_count** : Integer
