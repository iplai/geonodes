# Node Duplicate Elements

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeDuplicateElements`

```python
from geonodes import nodes

node = nodes.DuplicateElements(geometry=None, selection=None, amount=None, domain='POINT')
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean
- amount: Integer

#### Node parameter arguments:

- domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')

#### Output sockets:

- **geometry** : Geometry
- **duplicate_index** : Integer
