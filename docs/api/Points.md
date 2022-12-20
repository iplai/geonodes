# class Points

## title

- [(gen.fname(wnode)](domain_size-property)

## title

- [(gen.fname(wnode)](Points-classmethod)

## title


## title

- [(gen.fname(wnode)](instance_on_points)
- [(gen.fname(wnode)](set_point_radius)
- [(gen.fname(wnode)](to_vertices)
- [(gen.fname(wnode)](to_volume)
- [(gen.fname(wnode)](to_volume_amount)
- [(gen.fname(wnode)](to_volume_size)

## Points *classmethod*

{#Points}

> def Points(cls, count=None, position=None, radius=None):

Node [Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html) )

        ### Args:
- count: Integer
- position: Vector
- radius: Float

### Returns:

  socket 'geometry'

## domain_size *property*

{#domain_size}

> def domain_size(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

Node implemented as property.

### Returns:

  socket 'point_count'

## instance_on_points

{#instance_on_points}

> def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

        ### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:

  socket 'instances'

## set_point_radius

{#set_point_radius}

> def set_point_radius(self, selection=None, radius=None):

Node [Set Point Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html) )

        ### Args:
- selection: Boolean
- radius: Float

### Returns:

- node with sockets ['points']

## to_vertices

{#to_vertices}

> def to_vertices(self, points=None, selection=None):

Node [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html) )

        ### Args:
- points: Points
- selection: Boolean

### Returns:

  socket 'mesh' of class Mesh

## to_volume

{#to_volume}

> def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):

Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html) )

        ### Args:
- density: Float
- voxel_size: Float
- voxel_amount: Float
- radius: Float
- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

### Returns:

  socket 'volume' of class Volume

## to_volume_amount

{#to_volume_amount}

> def to_volume_amount(self, density=None, voxel_amount=None, radius=None):

Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html) )

        ### Args:
- density: Float
- voxel_amount: Float
- radius: Float

### Returns:

  socket 'volume' of class Volume

## to_volume_size

{#to_volume_size}

> def to_volume_size(self, density=None, voxel_size=None, radius=None):

Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html) )

        ### Args:
- density: Float
- voxel_size: Float
- radius: Float

### Returns:

  socket 'volume' of class Volume
