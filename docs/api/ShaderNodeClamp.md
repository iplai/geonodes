# Node Clamp

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)
- geonodes name: `WNode`
- bl_idname: `ShaderNodeClamp`

```python
from geonodes import nodes

node = nodes.Clamp(value=None, min=None, max=None, clamp_type='MINMAX')
```

#### Input socket arguments:

- value: Float
- min: Float
- max: Float

#### Node parameter arguments:

- clamp_type (str): Node parameter, default = 'MINMAX' in ('MINMAX', 'RANGE')

#### Output sockets:

- **result** : Float
