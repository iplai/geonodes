# Node Object Info

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeObjectInfo`

```python
from geonodes import nodes

node = nodes.ObjectInfo(object=None, as_instance=None, transform_space='ORIGINAL')
```

#### Input socket arguments:

- object: Object
- as_instance: Boolean

#### Node parameter arguments:

- transform_space (str): Node parameter, default = 'ORIGINAL' in ('ORIGINAL', 'RELATIVE')

#### Output sockets:

- **location** : Vector
- **rotation** : Vector
- **scale** : Vector
- **geometry** : Geometry
