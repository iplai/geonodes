# Node Slice String

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)
- geonodes name: `WNode`
- bl_idname: `FunctionNodeSliceString`

```python
from geonodes import nodes

node = nodes.SliceString(string=None, position=None, length=None)
```

#### Input socket arguments:

- string: String
- position: Integer
- length: Integer

#### Output sockets:

- **string** : String
