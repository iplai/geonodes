# Node ColorRamp

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
- geonodes name: `WNode`
- bl_idname: `ShaderNodeValToRGB`

```python
from geonodes import nodes

node = nodes.ColorRamp(fac=None)
```

#### Input socket arguments:

- fac: Float

#### Output sockets:

- **color** : Color
- **alpha** : Float
