# Node Trim Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeTrimCurve`

```python
from geonodes import nodes

node = nodes.TrimCurve(curve=None, start0=None, start1=None, end0=None, end1=None, mode='FACTOR')
```

#### Input socket arguments:

- curve: Curve
- start0: Float
- start1: Float
- end0: Float
- end1: Float

#### Node parameter arguments:

- mode (str): Node parameter, default = 'FACTOR' in ('FACTOR', 'LENGTH')

#### Output sockets:

- **curve** : Curve
