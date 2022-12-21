# Node Checker Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)
- geonodes name: `WNode`
- bl_idname: `ShaderNodeTexChecker`

```python
from geonodes import nodes

node = nodes.CheckerTexture(vector=None, color1=None, color2=None, scale=None)
```

#### Input socket arguments:

- vector: Vector
- color1: Color
- color2: Color
- scale: Float

#### Output sockets:

- **color** : Color
- **fac** : Float
