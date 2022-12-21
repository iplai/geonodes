# Node Viewer

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeViewer`

```python
from geonodes import nodes

node = nodes.Viewer(geometry=None, value=None, data_type='FLOAT', domain='AUTO')
```

#### Input socket arguments:

- geometry: Geometry
- value: `data_type` dependant

#### Node parameter arguments:

- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- domain (str): Node parameter, default = 'AUTO' in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')- Input sockets  : ['value']- Output sockets : []