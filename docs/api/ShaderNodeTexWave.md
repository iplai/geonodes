# Node Wave Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)
- geonodes name: `WNode`
- bl_idname: `ShaderNodeTexWave`

```python
from geonodes import nodes

node = nodes.WaveTexture(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS')
```

#### Input socket arguments:

- vector: Vector
- scale: Float
- distortion: Float
- detail: Float
- detail_scale: Float
- detail_roughness: Float
- phase_offset: Float

#### Node parameter arguments:

- bands_direction (str): Node parameter, default = 'X' in ('X', 'Y', 'Z', 'DIAGONAL')
- rings_direction (str): Node parameter, default = 'X' in ('X', 'Y', 'Z', 'SPHERICAL')
- wave_profile (str): Node parameter, default = 'SIN' in ('SIN', 'SAW', 'TRI')
- wave_type (str): Node parameter, default = 'BANDS' in ('BANDS', 'RINGS')

#### Output sockets:

- **color** : Color
- **fac** : Float
