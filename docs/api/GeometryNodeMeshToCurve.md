# Node Mesh to Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshToCurve`

```python
from geonodes import nodes

node = nodes.MeshToCurve(mesh=None, selection=None)
```

#### Input socket arguments:

- mesh: Mesh
- selection: Boolean

#### Output sockets:

- **curve** : Curve
