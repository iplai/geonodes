# Node Attribute Statistic

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeAttributeStatistic`

```python
from geonodes import nodes

node = nodes.AttributeStatistic(geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT')
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean
- attribute: `data_type` dependant

#### Node parameter arguments:

- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR')
- domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Output sockets:

- **mean** : ``data_type`` dependant
- **median** : ``data_type`` dependant
- **sum** : ``data_type`` dependant
- **min** : ``data_type`` dependant
- **max** : ``data_type`` dependant
- **range** : ``data_type`` dependant
- **standard_deviation** : ``data_type`` dependant
- **variance** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'FLOAT_VECTOR')- Input sockets  : ['attribute']- Output sockets : ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']