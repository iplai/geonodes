# Node Curve to Points

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeCurveToPoints`

```python
from geonodes import nodes

node = nodes.CurveToPoints(curve=None, count=None, length=None, mode='COUNT')
```

#### Input socket arguments:

- curve: Curve
- count: Integer
- length: Float

#### Node parameter arguments:

- mode (str): Node parameter, default = 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')

#### Output sockets:

- **points** : Points
- **tangent** : Vector
- **normal** : Vector
- **rotation** : Vector
