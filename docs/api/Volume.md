# class Volume

## title


## title

- [(gen.fname(wnode)](Cube-classmethod)

## title


## title

- [(gen.fname(wnode)](distribute_points)
- [(gen.fname(wnode)](distribute_points_grid)
- [(gen.fname(wnode)](distribute_points_random)
- [(gen.fname(wnode)](to_mesh)

## Cube *classmethod*

{#Cube}

> def Cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None):

Node [Volume Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_cube.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeCube.html) )

        ### Args:
- density: Float
- background: Float
- min: Vector
- max: Vector
- resolution_x: Integer
- resolution_y: Integer
- resolution_z: Integer

### Returns:

  socket 'volume'

## distribute_points

{#distribute_points}

> def distribute_points(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM'):

Node [Distribute Points in Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html) )

        ### Args:
- density: Float
- seed: Integer
- spacing: Vector
- threshold: Float
- mode (str): 'DENSITY_RANDOM' in [DENSITY_RANDOM, DENSITY_GRID]

### Returns:

  socket 'points' of class Points

## distribute_points_grid

{#distribute_points_grid}

> def distribute_points_grid(self, spacing=None, threshold=None):

Node [Distribute Points in Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html) )

        ### Args:
- spacing: Vector
- threshold: Float

### Returns:

  socket 'points' of class Points

## distribute_points_random

{#distribute_points_random}

> def distribute_points_random(self, density=None, seed=None):

Node [Distribute Points in Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html) )

        ### Args:
- density: Float
- seed: Integer

### Returns:

  socket 'points' of class Points

## to_mesh

{#to_mesh}

> def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):

Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_to_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeToMesh.html) )

        ### Args:
- voxel_size: Float
- voxel_amount: Float
- threshold: Float
- adaptivity: Float
- resolution_mode (str): 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]

### Returns:

  socket 'mesh' of class Mesh
