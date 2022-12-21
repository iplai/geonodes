# Node Set Material Index

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSetMaterialIndex`

```python
from geonodes import nodes

node = nodes.SetMaterialIndex(geometry=None, selection=None, material_index=None)
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean
- material_index: Integer

#### Output sockets:

- **geometry** : Geometry
