# class Rotation

## title


## title

- [(gen.fname(wnode)](AxisAngle-classmethod)
- [(gen.fname(wnode)](Euler-classmethod)

## title


## title

- [(gen.fname(wnode)](align_to_vector)
- [(gen.fname(wnode)](rotate_axis_angle)
- [(gen.fname(wnode)](rotate_euler)

## AxisAngle *classmethod*

{#AxisAngle}

> def AxisAngle(cls, rotation=None, axis=None, angle=None, space='OBJECT'):

Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html) )

        ### Args:
- rotation: Vector
- axis: Vector
- angle: Float
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:

  socket 'rotation'

## Euler *classmethod*

{#Euler}

> def Euler(cls, rotation=None, rotate_by=None, space='OBJECT'):

Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html) )

        ### Args:
- rotation: Vector
- rotate_by: Vector
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:

  socket 'rotation'

## align_to_vector

{#align_to_vector}

> def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):

Node [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html) )

        ### Args:
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

### Returns:

- node with sockets ['rotation']

## rotate_axis_angle

{#rotate_axis_angle}

> def rotate_axis_angle(self, axis=None, angle=None, space='OBJECT'):

Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html) )

        ### Args:
- axis: Vector
- angle: Float
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:

  socket 'rotation'

## rotate_euler

{#rotate_euler}

> def rotate_euler(self, rotate_by=None, space='OBJECT'):

Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html) )

        ### Args:
- rotate_by: Vector
- space (str): 'OBJECT' in [OBJECT, LOCAL]

### Returns:

  socket 'rotation'
