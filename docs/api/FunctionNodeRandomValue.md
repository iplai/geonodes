# Node Random Value

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
- geonodes name: `WNode`
- bl_idname: `FunctionNodeRandomValue`

```python
from geonodes import nodes

node = nodes.RandomValue(min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT')
```

#### Input socket arguments:

- min: `data_type` dependant
- max: `data_type` dependant
- probability: Float
- ID: Integer
- seed: Integer

#### Node parameter arguments:

- data_type (str): Node parameter, default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')

#### Output sockets:

- **value** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')- Input sockets  : ['min', 'max']- Output sockets : ['value']