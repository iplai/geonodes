# Node Distribute Points on Faces

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeDistributePointsOnFaces`

```python
from geonodes import nodes

node = nodes.DistributePointsOnFaces(mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM')
```

#### Input socket arguments:

- mesh: Mesh
- selection: Boolean
- distance_min: Float
- density_max: Float
- density: Float
- density_factor: Float
- seed: Integer

#### Node parameter arguments:

- distribute_method (str): Node parameter, default = 'RANDOM' in ('RANDOM', 'POISSON')

#### Output sockets:

- **points** : Points
- **normal** : Vector
- **rotation** : Vector
