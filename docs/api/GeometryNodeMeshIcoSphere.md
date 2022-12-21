# Node Ico Sphere

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshIcoSphere`

```python
from geonodes import nodes

node = nodes.IcoSphere(radius=None, subdivisions=None)
```

#### Input socket arguments:

- radius: Float
- subdivisions: Integer

#### Output sockets:

- **mesh** : Mesh
