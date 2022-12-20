# class Image

## title


## title


## title


## title

- [(gen.fname(wnode)](switch)
- [(gen.fname(wnode)](texture)

## switch

{#switch}

> def switch(self, switch=None, true=None):

Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## texture

{#texture}

> def texture(self, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):

Node [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html) )

        ### Args:
- vector: Vector
- frame: Integer
- extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
- interpolation (str): 'Linear' in [Linear, Closest, Cubic]

### Returns:

- tuple ('color', 'alpha')
