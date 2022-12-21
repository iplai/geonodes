# Node Join Strings

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeStringJoin`

```python
from geonodes import nodes

node = nodes.JoinStrings(*strings, delimiter=None)
```

#### Input socket arguments:

- delimiter: String
- strings: *String

#### Output sockets:

- **string** : String
