# Node Reverse Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/reverse_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeReverseCurve`

```python
from geonodes import nodes

node = nodes.ReverseCurve(curve=None, selection=None)
```

#### Input socket arguments:

- curve: Curve
- selection: Boolean

#### Output sockets:

- **curve** : Curve
