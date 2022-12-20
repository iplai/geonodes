# class Color

## title

- [(gen.fname(wnode)](alpha-property)
- [(gen.fname(wnode)](blue-property)
- [(gen.fname(wnode)](green-property)
- [(gen.fname(wnode)](hsl-property)
- [(gen.fname(wnode)](hsv-property)
- [(gen.fname(wnode)](hue-property)
- [(gen.fname(wnode)](lightness-property)
- [(gen.fname(wnode)](red-property)
- [(gen.fname(wnode)](rgb-property)
- [(gen.fname(wnode)](rgb_curves-property)
- [(gen.fname(wnode)](saturation-property)
- [(gen.fname(wnode)](value-property)

## title

- [(gen.fname(wnode)](Color-classmethod)
- [(gen.fname(wnode)](HSL-classmethod)
- [(gen.fname(wnode)](HSV-classmethod)
- [(gen.fname(wnode)](RGB-classmethod)

## title


## title

- [(gen.fname(wnode)](brighter)
- [(gen.fname(wnode)](compare)
- [(gen.fname(wnode)](darker)
- [(gen.fname(wnode)](equal)
- [(gen.fname(wnode)](equal)
- [(gen.fname(wnode)](mix)
- [(gen.fname(wnode)](mix_add)
- [(gen.fname(wnode)](mix_burn)
- [(gen.fname(wnode)](mix_color)
- [(gen.fname(wnode)](mix_darken)
- [(gen.fname(wnode)](mix_difference)
- [(gen.fname(wnode)](mix_divide)
- [(gen.fname(wnode)](mix_dodge)
- [(gen.fname(wnode)](mix_hue)
- [(gen.fname(wnode)](mix_lighten)
- [(gen.fname(wnode)](mix_linear_light)
- [(gen.fname(wnode)](mix_multiply)
- [(gen.fname(wnode)](mix_overlay)
- [(gen.fname(wnode)](mix_saturation)
- [(gen.fname(wnode)](mix_screen)
- [(gen.fname(wnode)](mix_soft_light)
- [(gen.fname(wnode)](mix_subtract)
- [(gen.fname(wnode)](mix_value)
- [(gen.fname(wnode)](switch)

## Color *classmethod*

{#Color}

> def Color(cls):

Node [Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html) )

### Returns:

  socket 'color'

## HSL *classmethod*

{#HSL}

> def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None):

Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

        ### Args:
- hue: Float
- saturation: Float
- lightness: Float
- alpha: Float

### Returns:

  socket 'color'

## HSV *classmethod*

{#HSV}

> def HSV(cls, hue=None, saturation=None, value=None, alpha=None):

Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

        ### Args:
- hue: Float
- saturation: Float
- value: Float
- alpha: Float

### Returns:

  socket 'color'

## RGB *classmethod*

{#RGB}

> def RGB(cls, red=None, green=None, blue=None, alpha=None):

Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

        ### Args:
- red: Float
- green: Float
- blue: Float
- alpha: Float

### Returns:

  socket 'color'

## alpha *property*

{#alpha}

> def alpha(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'alpha'

## blue *property*

{#blue}

> def blue(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'blue'

## brighter

{#brighter}

> def brighter(self, b=None):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## compare

{#compare}

> def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Returns:

  socket 'result'

## darker

{#darker}

> def darker(self, b=None):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

## equal

{#equal}

> def equal(self, b=None, epsilon=None):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## equal

{#equal}

> def equal(self, b=None, epsilon=None):

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

        ### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

## green *property*

{#green}

> def green(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'green'

## hsl *property*

{#hsl}

> def hsl(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

## hsv *property*

{#hsv}

> def hsv(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

## hue *property*

{#hue}

> def hue(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'red'

## lightness *property*

{#lightness}

> def lightness(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'blue'

## mix

{#mix}

> def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_add

{#mix_add}

> def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_burn

{#mix_burn}

> def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_color

{#mix_color}

> def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_darken

{#mix_darken}

> def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_difference

{#mix_difference}

> def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_divide

{#mix_divide}

> def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_dodge

{#mix_dodge}

> def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_hue

{#mix_hue}

> def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_lighten

{#mix_lighten}

> def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_linear_light

{#mix_linear_light}

> def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_multiply

{#mix_multiply}

> def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_overlay

{#mix_overlay}

> def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_saturation

{#mix_saturation}

> def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_screen

{#mix_screen}

> def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_soft_light

{#mix_soft_light}

> def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_subtract

{#mix_subtract}

> def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## mix_value

{#mix_value}

> def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False):

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

        ### Args:
- factor: ['Float', 'Vector']
- color: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

### Returns:

  socket 'result'

## red *property*

{#red}

> def red(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'red'

## rgb *property*

{#rgb}

> def rgb(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

- tuple ('red', 'green', 'blue', 'alpha')

## rgb_curves *property*

{#rgb_curves}

> def rgb_curves(self, fac=None):

Node [RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html) )

Node implemented as property.

### Returns:

- node with sockets ['color']

## saturation *property*

{#saturation}

> def saturation(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'green'

## switch

{#switch}

> def switch(self, switch=None, true=None):

Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

        ### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

## value *property*

{#value}

> def value(self):

Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

Node implemented as property.

### Returns:

  socket 'blue'
