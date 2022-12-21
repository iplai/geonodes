# Node Sample UV Surface

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_uv_surface.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSampleUVSurface`

```python
from geonodes import nodes

node = nodes.SampleUvSurface(mesh=None, value=None, source_uv_map=None, sample_uv=None, data_type='FLOAT')
```

#### Input socket arguments:

- mesh: Mesh
- value: `data_type` dependant
- source_uv_map: Vector
- sample_uv: Vector

#### Node parameter arguments:

- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

#### Output sockets:

- **value** : ``data_type`` dependant
- **is_valid** : Boolean

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')- Input sockets  : ['value']- Output sockets : ['value']