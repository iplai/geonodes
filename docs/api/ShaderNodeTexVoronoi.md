# Node Voronoi Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)
- geonodes name: `WNode`
- bl_idname: `ShaderNodeTexVoronoi`

```python
from geonodes import nodes

node = nodes.VoronoiTexture(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```

#### Input socket arguments:

- vector: Vector
- w: Float
- scale: Float
- smoothness: Float
- exponent: Float
- randomness: Float

#### Node parameter arguments:

- distance (str): Node parameter, default = 'EUCLIDEAN' in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
- feature (str): Node parameter, default = 'F1' in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
- voronoi_dimensions (str): Node parameter, default = '3D' in ('1D', '2D', '3D', '4D')

#### Output sockets:

- **distance** : Float
- **color** : Color
- **position** : Vector
- **w** : Float
- **radius** : Float
