# Node Sample Index

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSampleIndex`

```python
from geonodes import nodes

node = nodes.SampleIndex(geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT')
```

#### Input socket arguments:

- geometry: Geometry
- value: `data_type` dependant
- index: Integer

#### Node parameter arguments:

- clamp (bool): Node parameter, default = False
- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- domain (str): Node parameter, default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Output sockets:

- **value** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')- Input sockets  : ['value']- Output sockets : ['value']