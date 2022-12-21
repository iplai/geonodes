# Node Separate Geometry

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSeparateGeometry`

```python
from geonodes import nodes

node = nodes.SeparateGeometry(geometry=None, selection=None, domain='POINT')
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean

#### Node parameter arguments:

- domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')

#### Output sockets:

- **selection** : Geometry
- **inverted** : Geometry
