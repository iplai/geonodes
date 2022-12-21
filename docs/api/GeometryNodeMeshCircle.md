# Node Mesh Circle

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshCircle`

```python
from geonodes import nodes

node = nodes.MeshCircle(vertices=None, radius=None, fill_type='NONE')
```

#### Input socket arguments:

- vertices: Integer
- radius: Float

#### Node parameter arguments:

- fill_type (str): Node parameter, default = 'NONE' in ('NONE', 'NGON', 'TRIANGLE_FAN')

#### Output sockets:

- **mesh** : Mesh
