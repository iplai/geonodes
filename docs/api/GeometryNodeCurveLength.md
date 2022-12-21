# Node Curve Length

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_length.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeCurveLength`

```python
from geonodes import nodes

node = nodes.CurveLength(curve=None)
```

#### Input socket arguments:

- curve: Curve

#### Output sockets:

- **length** : Float
