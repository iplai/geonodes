# Nodes Menus

- [Attribute](#menu-Attribute)
- [Color](#menu-Color)
- [Curve](#menu-Curve)
- [Curve Primitives](#menu-Curve-Primitives)
- [Curve Topology](#menu-Curve-Topology)
- [Geometry](#menu-Geometry)
- [Input](#menu-Input)
- [Instances](#menu-Instances)
- [Material](#menu-Material)
- [Mesh](#menu-Mesh)
- [Mesh Primitives](#menu-Mesh-Primitives)
- [Point](#menu-Point)
- [Text](#menu-Text)
- [Texture](#menu-Texture)
- [Utilities](#menu-Utilities)
- [UV](#menu-UV)
- [Vector](#menu-Vector)
- [Volume](#menu-Volume)

## Menu Attribute

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Attribute Statistic](#nodes) | [Domain](Domain.md) | [attribute_statistic](Domain.md#attribute_statistic) / [attribute_mean](Domain.md#attribute_mean) / [attribute_median](Domain.md#attribute_median) / [attribute_sum](Domain.md#attribute_sum) / [attribute_min](Domain.md#attribute_min) / [attribute_max](Domain.md#attribute_max) / [attribute_range](Domain.md#attribute_range) / [attribute_std](Domain.md#attribute_std) / [attribute_var](Domain.md#attribute_var) / |
|      | [Geometry](Geometry.md) | [attribute_statistic](Geometry.md#attribute_statistic) |
| [Capture Attribute](#nodes) | [Domain](Domain.md) | [capture_attribute](Domain.md#capture_attribute) |
|      | [Geometry](Geometry.md) | - [capture_attribute](Geometry.md#capture_attribute)<br>- [capture_attribute_node](Geometry.md#capture_attribute_node)|
| [Domain Size](#nodes) | [CloudPoint](CloudPoint.md) | [domain_size](CloudPoint.md#domain_size) |
|      | [ControlPoint](ControlPoint.md) | [domain_size](ControlPoint.md#domain_size) |
|      | [Corner](Corner.md) | [domain_size](Corner.md#domain_size) |
|      | [Curve](Curve.md) | - [domain_size](Curve.md#domain_size-property)<br>- [point_count](Curve.md#point_count-property)<br>- [spline_count](Curve.md#spline_count-property)|
|      | [Edge](Edge.md) | [domain_size](Edge.md#domain_size) |
|      | [Face](Face.md) | [domain_size](Face.md#domain_size) |
|      | [Geometry](Geometry.md) | [domain_size](Geometry.md#domain_size-property) |
|      | [Instance](Instance.md) | [domain_size](Instance.md#domain_size) |
|      | [Instances](Instances.md) | [domain_size](Instances.md#domain_size-property) |
|      | [Mesh](Mesh.md) | [domain_size](Mesh.md#domain_size-property) / [point_count](Mesh.md#point_count-property) / [face_count](Mesh.md#face_count-property) / [edge_count](Mesh.md#edge_count-property) / [corner_count](Mesh.md#corner_count-property) / |
|      | [Points](Points.md) | [domain_size](Points.md#domain_size-property) |
|      | [Spline](Spline.md) | [domain_size](Spline.md#domain_size) |
|      | [Vertex](Vertex.md) | [domain_size](Vertex.md#domain_size) |
| [Store Named Attribute](#nodes) | [Domain](Domain.md) | [store_named_attribute](Domain.md#store_named_attribute) / [set_named_boolean](Domain.md#set_named_boolean) / [set_named_integer](Domain.md#set_named_integer) / [set_named_float](Domain.md#set_named_float) / [set_named_vector](Domain.md#set_named_vector) / [set_named_color](Domain.md#set_named_color) / |
|      | [Geometry](Geometry.md) | [store_named_attribute](Geometry.md#store_named_attribute) / [set_named_boolean](Geometry.md#set_named_boolean) / [set_named_integer](Geometry.md#set_named_integer) / [set_named_float](Geometry.md#set_named_float) / [set_named_vector](Geometry.md#set_named_vector) / [set_named_color](Geometry.md#set_named_color) / |
| [Remove Named Attribute](#nodes) | [Domain](Domain.md) | [remove_named_attribute](Domain.md#remove_named_attribute) |
|      | [Geometry](Geometry.md) | [remove_named_attribute](Geometry.md#remove_named_attribute) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Color

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [ColorRamp](#nodes) | [Float](Float.md) | [color_ramp](Float.md#color_ramp-property) |
|      | [function](function.md) | [color_ramp](function.md#color_ramp) |
| [Combine Color](#nodes) | [Color](Color.md) | - [RGB](Color.md#RGB-classmethod)<br>- [HSV](Color.md#HSV-classmethod)<br>- [HSL](Color.md#HSL-classmethod)|
|      | [function](function.md) | - [combine_rgb](function.md#combine_rgb)<br>- [combine_hsv](function.md#combine_hsv)<br>- [combine_hsl](function.md#combine_hsl)|
| [Mix](#nodes) | [Color](Color.md) | [mix](Color.md#mix) / [mix_darken](Color.md#mix_darken) / [mix_multiply](Color.md#mix_multiply) / [mix_burn](Color.md#mix_burn) / [mix_lighten](Color.md#mix_lighten) / [mix_screen](Color.md#mix_screen) / [mix_dodge](Color.md#mix_dodge) / [mix_add](Color.md#mix_add) / [mix_overlay](Color.md#mix_overlay) / [mix_soft_light](Color.md#mix_soft_light) / [mix_linear_light](Color.md#mix_linear_light) / [mix_difference](Color.md#mix_difference) / [mix_subtract](Color.md#mix_subtract) / [mix_divide](Color.md#mix_divide) / [mix_hue](Color.md#mix_hue) / [mix_saturation](Color.md#mix_saturation) / [mix_color](Color.md#mix_color) / [mix_value](Color.md#mix_value) / |
|      | [Float](Float.md) | [mix](Float.md#mix) |
|      | [Vector](Vector.md) | - [mix](Vector.md#mix)<br>- [mix_uniform](Vector.md#mix_uniform)<br>- [mix_non_uniform](Vector.md#mix_non_uniform)|
|      | [function](function.md) | [float_mix](function.md#float_mix) / [vector_mix](function.md#vector_mix) / [color_mix](function.md#color_mix) / [color_darken](function.md#color_darken) / [color_multiply](function.md#color_multiply) / [color_burn](function.md#color_burn) / [color_lighten](function.md#color_lighten) / [color_screen](function.md#color_screen) / [color_dodge](function.md#color_dodge) / [color_add](function.md#color_add) / [color_overlay](function.md#color_overlay) / [color_soft_light](function.md#color_soft_light) / [color_linear_light](function.md#color_linear_light) / [color_difference](function.md#color_difference) / [color_subtract](function.md#color_subtract) / [color_divide](function.md#color_divide) / [color_hue](function.md#color_hue) / [color_saturation](function.md#color_saturation) / [color_color](function.md#color_color) / [color_value](function.md#color_value) / |
| [RGB Curves](#nodes) | [Color](Color.md) | [rgb_curves](Color.md#rgb_curves-property) |
|      | [function](function.md) | [rgb_curves](function.md#rgb_curves) |
| [Separate Color](#nodes) | [Color](Color.md) | [rgb](Color.md#rgb-property) / [hsv](Color.md#hsv-property) / [hsl](Color.md#hsl-property) / [alpha](Color.md#alpha-property) / [red](Color.md#red-property) / [green](Color.md#green-property) / [blue](Color.md#blue-property) / [hue](Color.md#hue-property) / [saturation](Color.md#saturation-property) / [value](Color.md#value-property) / [lightness](Color.md#lightness-property) / |
|      | [function](function.md) | - [separate_rgb](function.md#separate_rgb)<br>- [separate_hsv](function.md#separate_hsv)<br>- [separate_hsl](function.md#separate_hsl)|

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Curve Length](#nodes) | [Curve](Curve.md) | [length](Curve.md#length-property) |
| [Curve to Mesh](#nodes) | [Curve](Curve.md) | [to_mesh](Curve.md#to_mesh) |
| [Curve to Points](#nodes) | [Curve](Curve.md) | - [to_points](Curve.md#to_points)<br>- [to_points_count](Curve.md#to_points_count)<br>- [to_points_length](Curve.md#to_points_length)<br>- [to_points_evaluated](Curve.md#to_points_evaluated)|
| [Deform Curves on Surface](#nodes) | [Curve](Curve.md) | [deform_on_surface](Curve.md#deform_on_surface) |
| [Fill Curve](#nodes) | [Curve](Curve.md) | - [fill](Curve.md#fill)<br>- [fill_triangles](Curve.md#fill_triangles)<br>- [fill_ngons](Curve.md#fill_ngons)|
| [Fillet Curve](#nodes) | [Curve](Curve.md) | - [fillet](Curve.md#fillet)<br>- [fillet_bezier](Curve.md#fillet_bezier)<br>- [fillet_poly](Curve.md#fillet_poly)|
| [Resample Curve](#nodes) | [Curve](Curve.md) | - [resample](Curve.md#resample)<br>- [resample_count](Curve.md#resample_count)<br>- [resample_length](Curve.md#resample_length)<br>- [resample_evaluated](Curve.md#resample_evaluated)|
|      | [Spline](Spline.md) | - [resample](Spline.md#resample)<br>- [resample_count](Spline.md#resample_count)<br>- [resample_length](Spline.md#resample_length)<br>- [resample_evaluated](Spline.md#resample_evaluated)|
| [Reverse Curve](#nodes) | [Curve](Curve.md) | [reverse](Curve.md#reverse) |
| [Sample Curve](#nodes) | [Curve](Curve.md) | [sample](Curve.md#sample) |
| [Subdivide Curve](#nodes) | [Curve](Curve.md) | [subdivide](Curve.md#subdivide) |
| [Trim Curve](#nodes) | [Curve](Curve.md) | - [trim](Curve.md#trim)<br>- [trim_factor](Curve.md#trim_factor)<br>- [trim_length](Curve.md#trim_length)|
| [Curve Handle Positions](#nodes) | [ControlPoint](ControlPoint.md) | - [handle_positions](ControlPoint.md#handle_positions)<br>- [left_handle_positions](ControlPoint.md#left_handle_positions-property)<br>- [right_handle_positions](ControlPoint.md#right_handle_positions-property)|
| [Curve Tangent](#nodes) | [ControlPoint](ControlPoint.md) | [tangent](ControlPoint.md#tangent-property) |
| [Curve Tilt](#nodes) | [ControlPoint](ControlPoint.md) | [tilt](ControlPoint.md#tilt-property) |
| [Endpoint Selection](#nodes) | [ControlPoint](ControlPoint.md) | [endpoint_selection](ControlPoint.md#endpoint_selection) |
| [Handle Type Selection](#nodes) | [ControlPoint](ControlPoint.md) | [handle_type_selection_node](ControlPoint.md#handle_type_selection_node) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / |
| [Is Spline Cyclic](#nodes) | [Spline](Spline.md) | [cyclic](Spline.md#cyclic-property) |
| [Spline Length](#nodes) | [Spline](Spline.md) | [length](Spline.md#length-property) |
| [Spline Parameter](#nodes) | [ControlPoint](ControlPoint.md) | - [parameter](ControlPoint.md#parameter-property)<br>- [parameter_factor](ControlPoint.md#parameter_factor-property)<br>- [parameter_length](ControlPoint.md#parameter_length-property)<br>- [parameter_index](ControlPoint.md#parameter_index-property)|
| [Spline Resolution](#nodes) | [Spline](Spline.md) | [resolution](Spline.md#resolution-property) |
| [Set Curve Normal](#nodes) | [Spline](Spline.md) | - [set_normal](Spline.md#set_normal)<br>- [normal](Spline.md#normal)|
| [Set Curve Radius](#nodes) | [ControlPoint](ControlPoint.md) | - [set_radius](ControlPoint.md#set_radius)<br>- [radius](ControlPoint.md#radius)|
| [Set Curve Tilt](#nodes) | [ControlPoint](ControlPoint.md) | - [set_tilt](ControlPoint.md#set_tilt)<br>- [tilt](ControlPoint.md#tilt)|
| [Set Handle Positions](#nodes) | [ControlPoint](ControlPoint.md) | [set_handle_positions](ControlPoint.md#set_handle_positions) / [set_handle_positions_left](ControlPoint.md#set_handle_positions_left) / [set_handle_positions_right](ControlPoint.md#set_handle_positions_right) / [left_handle_positions](ControlPoint.md#left_handle_positions) / [right_handle_positions](ControlPoint.md#right_handle_positions) / |
| [Set Handle Type](#nodes) | [ControlPoint](ControlPoint.md) | - [set_handle_type_node](ControlPoint.md#set_handle_type_node)<br>- [set_handle_type](ControlPoint.md#set_handle_type)|
| [Set Spline Cyclic](#nodes) | [Spline](Spline.md) | - [set_cyclic](Spline.md#set_cyclic)<br>- [cyclic](Spline.md#cyclic)|
| [Set Spline Resolution](#nodes) | [Spline](Spline.md) | - [set_resolution](Spline.md#set_resolution)<br>- [resolution](Spline.md#resolution)|
| [Set Spline Type](#nodes) | [Spline](Spline.md) | - [set_type](Spline.md#set_type)<br>- [type](Spline.md#type-property)<br>- [type](Spline.md#type)|

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Curve Primitives

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Arc](#nodes) | [Curve](Curve.md) | - [Arc](Curve.md#Arc-classmethod)<br>- [ArcFromPoints](Curve.md#ArcFromPoints-classmethod)|
| [Bezier Segment](#nodes) | [Curve](Curve.md) | [bezier_segment](Curve.md#bezier_segment-classmethod) |
| [Curve Circle](#nodes) | [Curve](Curve.md) | - [Circle](Curve.md#Circle-classmethod)<br>- [CircleFromPoints](Curve.md#CircleFromPoints-classmethod)|
| [Curve Line](#nodes) | [Curve](Curve.md) | - [Line](Curve.md#Line-classmethod)<br>- [LineDirection](Curve.md#LineDirection-classmethod)|
| [Spiral](#nodes) | [Curve](Curve.md) | [Spiral](Curve.md#Spiral-classmethod) |
| [Quadratic Bezier](#nodes) | [Curve](Curve.md) | [QuadraticBezier](Curve.md#QuadraticBezier-classmethod) |
| [Quadrilateral](#nodes) | [Curve](Curve.md) | [Quadrilateral](Curve.md#Quadrilateral-classmethod) |
| [Star](#nodes) | [Curve](Curve.md) | [Star](Curve.md#Star-classmethod) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Curve Topology

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Offset Point in Curve](#nodes) | [ControlPoint](ControlPoint.md) | [offset](ControlPoint.md#offset) |
|      | [Curve](Curve.md) | [offset_point](Curve.md#offset_point) |
| [Curve of Point](#nodes) | [ControlPoint](ControlPoint.md) | [curve](ControlPoint.md#curve) |
|      | [Curve](Curve.md) | [curve_of_point](Curve.md#curve_of_point) |
| [Points of Curve](#nodes) | [Curve](Curve.md) | [points_of_curve](Curve.md#points_of_curve) |
|      | [Spline](Spline.md) | [points](Spline.md#points) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Geometry

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Bounding Box](#nodes) | [Geometry](Geometry.md) | - [bounding_box](Geometry.md#bounding_box-property)<br>- [bounding_box_min](Geometry.md#bounding_box_min-property)<br>- [bounding_box_min](Geometry.md#bounding_box_min-property)|
| [Convex Hull](#nodes) | [Geometry](Geometry.md) | [convex_hull](Geometry.md#convex_hull-property) |
| [Delete Geometry](#nodes) | [Domain](Domain.md) | [delete](Domain.md#delete) |
|      | [Edge](Edge.md) | - [delete_all](Edge.md#delete_all)<br>- [delete_edges](Edge.md#delete_edges)<br>- [delete_faces](Edge.md#delete_faces)|
|      | [Face](Face.md) | - [delete_all](Face.md#delete_all)<br>- [delete_edges](Face.md#delete_edges)<br>- [delete_faces](Face.md#delete_faces)|
|      | [Geometry](Geometry.md) | [delete](Geometry.md#delete) |
|      | [Mesh](Mesh.md) | - [delete_all](Mesh.md#delete_all)<br>- [delete_edges](Mesh.md#delete_edges)<br>- [delete_faces](Mesh.md#delete_faces)|
|      | [Vertex](Vertex.md) | - [delete_all](Vertex.md#delete_all)<br>- [delete_edges](Vertex.md#delete_edges)<br>- [delete_faces](Vertex.md#delete_faces)|
| [Duplicate Elements](#nodes) | [Domain](Domain.md) | [duplicate](Domain.md#duplicate) |
|      | [Geometry](Geometry.md) | [duplicate](Geometry.md#duplicate) |
| [Geometry Proximity](#nodes) | [Geometry](Geometry.md) | - [proximity](Geometry.md#proximity)<br>- [proximity_points](Geometry.md#proximity_points)<br>- [proximity_edges](Geometry.md#proximity_edges)<br>- [proximity_facess](Geometry.md#proximity_facess)|
| [Geometry to Instance](#nodes) | [Geometry](Geometry.md) | [to_instance](Geometry.md#to_instance) |
|      | [function](function.md) | [geometry_to_instance](function.md#geometry_to_instance) |
| [Join Geometry](#nodes) | [Geometry](Geometry.md) | [join](Geometry.md#join) |
|      | [function](function.md) | [join_geometry](function.md#join_geometry) |
| [Merge by Distance](#nodes) | [Geometry](Geometry.md) | [merge_by_distance](Geometry.md#merge_by_distance) |
|      | [Vertex](Vertex.md) | [merge_by_distance](Vertex.md#merge_by_distance) |
| [Raycast](#nodes) | [Geometry](Geometry.md) | - [raycast](Geometry.md#raycast)<br>- [raycast_interpolated](Geometry.md#raycast_interpolated)<br>- [raycast_nearest](Geometry.md#raycast_nearest)|
| [Sample Index](#nodes) | [Domain](Domain.md) | [sample_index](Domain.md#sample_index) |
|      | [Geometry](Geometry.md) | [sample_index](Geometry.md#sample_index) |
| [Sample Nearest](#nodes) | [Domain](Domain.md) | [sample_nearest](Domain.md#sample_nearest) |
|      | [Geometry](Geometry.md) | [sample_nearest](Geometry.md#sample_nearest) |
| [Separate Components](#nodes) | [Geometry](Geometry.md) | [separate_components](Geometry.md#separate_components-property) / [mesh_component](Geometry.md#mesh_component-property) / [curve_component](Geometry.md#curve_component-property) / [points_component](Geometry.md#points_component-property) / [volume_component](Geometry.md#volume_component-property) / [instances_component](Geometry.md#instances_component-property) / |
| [Separate Geometry](#nodes) | [Domain](Domain.md) | [separate](Domain.md#separate) |
|      | [Geometry](Geometry.md) | [separate](Geometry.md#separate) |
| [Transform](#nodes) | [Geometry](Geometry.md) | [transform](Geometry.md#transform) |
| [Set ID](#nodes) | [Domain](Domain.md) | - [set_ID](Domain.md#set_ID)<br>- [ID](Domain.md#ID)|
|      | [Geometry](Geometry.md) | [set_ID](Geometry.md#set_ID) |
| [Set Position](#nodes) | [Domain](Domain.md) | - [set_position](Domain.md#set_position)<br>- [position](Domain.md#position)|
|      | [Geometry](Geometry.md) | [set_position](Geometry.md#set_position) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Input

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Boolean](#nodes) | [Boolean](Boolean.md) | [Boolean](Boolean.md#Boolean-classmethod) |
| [Collection Info](#nodes) | [Geometry](Geometry.md) | [Collection](Geometry.md#Collection-classmethod) |
| [Color](#nodes) | [Color](Color.md) | [Color](Color.md#Color-classmethod) |
| [Integer](#nodes) | [Integer](Integer.md) | [Integer](Integer.md#Integer-classmethod) |
| [Is Viewport](#nodes) | [Geometry](Geometry.md) | [is_viewport](Geometry.md#is_viewport-property) |
| [Material](#nodes) | [Material](Material.md) | [Material](Material.md#Material-classmethod) |
| [Object Info](#nodes) | [Object](Object.md) | [info](Object.md#info) / [location](Object.md#location) / [rotation](Object.md#rotation) / [scale](Object.md#scale) / [geometry](Object.md#geometry) / |
| [Self Object](#nodes) | [Object](Object.md) | [Self](Object.md#Self-classmethod) |
| [String](#nodes) | [String](String.md) | [String](String.md#String-classmethod) |
| [Value](#nodes) | [Float](Float.md) | [Value](Float.md#Value-classmethod) |
| [Vector](#nodes) | [Vector](Vector.md) | [Vector](Vector.md#Vector-classmethod) |
| [ID](#nodes) | [Domain](Domain.md) | [ID](Domain.md#ID-property) |
|      | [Geometry](Geometry.md) | [ID](Geometry.md#ID-property) |
| [Index](#nodes) | [Domain](Domain.md) | - [index](Domain.md#index-property)<br>- [domain_index](Domain.md#domain_index-property)|
|      | [Geometry](Geometry.md) | [index](Geometry.md#index-property) |
| [Named Attribute](#nodes) | [Domain](Domain.md) | [named_attribute](Domain.md#named_attribute) / [get_named_float](Domain.md#get_named_float) / [get_named_integer](Domain.md#get_named_integer) / [get_named_vector](Domain.md#get_named_vector) / [get_named_color](Domain.md#get_named_color) / [get_named_boolean](Domain.md#get_named_boolean) / |
|      | [Geometry](Geometry.md) | [named_attribute](Geometry.md#named_attribute) / [get_named_float](Geometry.md#get_named_float) / [get_named_integer](Geometry.md#get_named_integer) / [get_named_vector](Geometry.md#get_named_vector) / [get_named_color](Geometry.md#get_named_color) / [get_named_boolean](Geometry.md#get_named_boolean) / |
| [Normal](#nodes) | [Domain](Domain.md) | [normal](Domain.md#normal-property) |
|      | [Geometry](Geometry.md) | [normal](Geometry.md#normal-property) |
|      | [Spline](Spline.md) | [normal](Spline.md#normal-property) |
| [Position](#nodes) | [Domain](Domain.md) | [position](Domain.md#position-property) |
|      | [Geometry](Geometry.md) | [position](Geometry.md#position-property) |
| [Radius](#nodes) | [CloudPoint](CloudPoint.md) | [radius](CloudPoint.md#radius-property) |
|      | [ControlPoint](ControlPoint.md) | [radius](ControlPoint.md#radius-property) |
|      | [Geometry](Geometry.md) | [radius](Geometry.md#radius-property) |
| [Scene Time](#nodes) | [Float](Float.md) | - [Seconds](Float.md#Seconds-classmethod)<br>- [Frame](Float.md#Frame-classmethod)|

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Instances

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Instance on Points](#nodes) | [CloudPoint](CloudPoint.md) | [instance_on_points](CloudPoint.md#instance_on_points) |
|      | [ControlPoint](ControlPoint.md) | [instance_on_points](ControlPoint.md#instance_on_points) |
|      | [Curve](Curve.md) | [instance_on_points](Curve.md#instance_on_points) |
|      | [Instances](Instances.md) | - [InstanceOnPoints](Instances.md#InstanceOnPoints-classmethod)<br>- [on_points](Instances.md#on_points)|
|      | [Mesh](Mesh.md) | [instance_on_points](Mesh.md#instance_on_points) |
|      | [Points](Points.md) | [instance_on_points](Points.md#instance_on_points) |
|      | [Vertex](Vertex.md) | [instance_on_points](Vertex.md#instance_on_points) |
| [Instances to Points](#nodes) | [Instance](Instance.md) | [to_points](Instance.md#to_points) |
|      | [Instances](Instances.md) | [to_points](Instances.md#to_points) |
| [Realize Instances](#nodes) | [Instances](Instances.md) | [realize](Instances.md#realize) |
| [Rotate Instances](#nodes) | [Instance](Instance.md) | [rotate](Instance.md#rotate) |
|      | [Instances](Instances.md) | [rotate](Instances.md#rotate) |
| [Scale Instances](#nodes) | [Instance](Instance.md) | [set_scale](Instance.md#set_scale) |
|      | [Instances](Instances.md) | [set_scale](Instances.md#set_scale) |
| [Translate Instances](#nodes) | [Instance](Instance.md) | [translate](Instance.md#translate) |
|      | [Instances](Instances.md) | [translate](Instances.md#translate) |
| [Instance Scale](#nodes) | [Instance](Instance.md) | [scale](Instance.md#scale-property) |
|      | [Instances](Instances.md) | [scale](Instances.md#scale-property) |
| [Instance Rotation](#nodes) | [Instance](Instance.md) | [rotation](Instance.md#rotation-property) |
|      | [Instances](Instances.md) | [rotation](Instances.md#rotation-property) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Material

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Replace Material](#nodes) | [Geometry](Geometry.md) | [replace_material](Geometry.md#replace_material) |
| [Material Index](#nodes) | [Domain](Domain.md) | [material_index](Domain.md#material_index-property) |
|      | [Geometry](Geometry.md) | [material_index](Geometry.md#material_index-property) |
| [Material Selection](#nodes) | [Domain](Domain.md) | [material_selection](Domain.md#material_selection) |
|      | [Geometry](Geometry.md) | [material_selection](Geometry.md#material_selection) |
| [Set Material](#nodes) | [Face](Face.md) | - [set_material](Face.md#set_material)<br>- [material](Face.md#material-property)<br>- [material](Face.md#material)|
|      | [Geometry](Geometry.md) | [set_material](Geometry.md#set_material) |
|      | [Spline](Spline.md) | - [set_material](Spline.md#set_material)<br>- [material](Spline.md#material-property)<br>- [material](Spline.md#material)|
| [Set Material Index](#nodes) | [Domain](Domain.md) | [set_material_index](Domain.md#set_material_index) |
|      | [Geometry](Geometry.md) | [set_material_index](Geometry.md#set_material_index) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Mesh

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Dual Mesh](#nodes) | [Mesh](Mesh.md) | [dual_mesh](Mesh.md#dual_mesh) |
| [Edge Paths to Curves](#nodes) | [Edge](Edge.md) | [edge_paths_to_curves](Edge.md#edge_paths_to_curves) |
|      | [Mesh](Mesh.md) | [edge_paths_to_curves](Mesh.md#edge_paths_to_curves) |
| [Edge Paths to Selection](#nodes) | [Mesh](Mesh.md) | [edge_paths_to_selection](Mesh.md#edge_paths_to_selection) |
| [Extrude Mesh](#nodes) | [Edge](Edge.md) | [extrude](Edge.md#extrude) |
|      | [Face](Face.md) | [extrude](Face.md#extrude) |
|      | [Mesh](Mesh.md) | [extrude](Mesh.md#extrude) |
|      | [Vertex](Vertex.md) | [extrude](Vertex.md#extrude) |
| [Flip Faces](#nodes) | [Face](Face.md) | [flip](Face.md#flip) |
|      | [Mesh](Mesh.md) | [flip_faces](Mesh.md#flip_faces) |
| [Mesh Boolean](#nodes) | [Mesh](Mesh.md) | - [boolean_intersect](Mesh.md#boolean_intersect)<br>- [boolean_union](Mesh.md#boolean_union)<br>- [boolean_difference](Mesh.md#boolean_difference)|
| [Mesh to Curve](#nodes) | [Edge](Edge.md) | [to_curve](Edge.md#to_curve) |
|      | [Mesh](Mesh.md) | [to_curve](Mesh.md#to_curve) |
| [Mesh to Points](#nodes) | [Mesh](Mesh.md) | [to_points](Mesh.md#to_points) |
|      | [Vertex](Vertex.md) | [to_points](Vertex.md#to_points) |
| [Mesh to Volume](#nodes) | [Mesh](Mesh.md) | [to_volume](Mesh.md#to_volume) |
|      | [Vertex](Vertex.md) | [to_volume](Vertex.md#to_volume) |
| [Sample Nearest Surface](#nodes) | [Mesh](Mesh.md) | [sample_nearest_surface](Mesh.md#sample_nearest_surface) |
| [Sample UV Surface](#nodes) | [Mesh](Mesh.md) | [sample_uv_surface](Mesh.md#sample_uv_surface) |
| [Scale Elements](#nodes) | [Edge](Edge.md) | - [scale_uniform](Edge.md#scale_uniform)<br>- [scale_single_axis](Edge.md#scale_single_axis)|
|      | [Face](Face.md) | - [scale_uniform](Face.md#scale_uniform)<br>- [scale_single_axis](Face.md#scale_single_axis)|
|      | [Mesh](Mesh.md) | - [scale_elements](Mesh.md#scale_elements)<br>- [scale_uniform](Mesh.md#scale_uniform)<br>- [scale_single_axis](Mesh.md#scale_single_axis)|
| [Split Edges](#nodes) | [Edge](Edge.md) | [split](Edge.md#split) |
|      | [Mesh](Mesh.md) | [split_edges](Mesh.md#split_edges) |
| [Subdivide Mesh](#nodes) | [Mesh](Mesh.md) | [subdivide](Mesh.md#subdivide) |
| [Subdivision Surface](#nodes) | [Mesh](Mesh.md) | [subdivision_surface](Mesh.md#subdivision_surface) |
| [Triangulate](#nodes) | [Face](Face.md) | [triangulate](Face.md#triangulate) |
|      | [Mesh](Mesh.md) | [triangulate](Mesh.md#triangulate) |
| [Edge Angle](#nodes) | [Edge](Edge.md) | - [angle](Edge.md#angle-property)<br>- [unsigned_angle](Edge.md#unsigned_angle-property)<br>- [signed_angle](Edge.md#signed_angle-property)|
| [Edge Neighbors](#nodes) | [Edge](Edge.md) | [neighbors](Edge.md#neighbors-property) |
| [Edge Vertices](#nodes) | [Edge](Edge.md) | - [vertices](Edge.md#vertices-property)<br>- [vertices_index](Edge.md#vertices_index-property)<br>- [vertices_position](Edge.md#vertices_position-property)|
| [Face Area](#nodes) | [Face](Face.md) | [area](Face.md#area-property) |
| [Face Neighbors](#nodes) | [Face](Face.md) | - [neighbors](Face.md#neighbors-property)<br>- [neighbors_vertex_count](Face.md#neighbors_vertex_count-property)<br>- [neighbors_face_count](Face.md#neighbors_face_count-property)|
| [Face Set Boundaries](#nodes) | [Face](Face.md) | [face_set_boundaries](Face.md#face_set_boundaries) |
|      | [Mesh](Mesh.md) | [face_set_boundaries](Mesh.md#face_set_boundaries) |
| [Face is Planar](#nodes) | [Face](Face.md) | [is_planar](Face.md#is_planar) |
|      | [Mesh](Mesh.md) | [face_is_planar](Mesh.md#face_is_planar) |
| [Is Shade Smooth](#nodes) | [Face](Face.md) | [shade_smooth](Face.md#shade_smooth-property) |
|      | [Mesh](Mesh.md) | [is_shade_smooth](Mesh.md#is_shade_smooth) |
| [Mesh Island](#nodes) | [Face](Face.md) | - [island](Face.md#island-property)<br>- [island_index](Face.md#island_index-property)<br>- [island_count](Face.md#island_count-property)|
|      | [Mesh](Mesh.md) | - [island](Mesh.md#island-property)<br>- [island_index](Mesh.md#island_index-property)<br>- [island_count](Mesh.md#island_count-property)|
| [Shortest Edge Paths](#nodes) | [Mesh](Mesh.md) | [shortest_edge_paths](Mesh.md#shortest_edge_paths) |
| [Vertex Neighbors](#nodes) | [Vertex](Vertex.md) | - [neighbors](Vertex.md#neighbors-property)<br>- [neighbors_vertex_count](Vertex.md#neighbors_vertex_count-property)<br>- [neighbors_face_count](Vertex.md#neighbors_face_count-property)|
| [Set Shade Smooth](#nodes) | [Face](Face.md) | - [set_shade_smooth](Face.md#set_shade_smooth)<br>- [shade_smooth](Face.md#shade_smooth)|
|      | [Mesh](Mesh.md) | [set_shade_smooth](Mesh.md#set_shade_smooth) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Mesh Primitives

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Cone](#nodes) | [Mesh](Mesh.md) | [Cone](Mesh.md#Cone-staticmethod) |
| [Cube](#nodes) | [Mesh](Mesh.md) | [Cube](Mesh.md#Cube-classmethod) |
| [Cylinder](#nodes) | [Mesh](Mesh.md) | [Cylinder](Mesh.md#Cylinder-staticmethod) |
| [Grid](#nodes) | [Mesh](Mesh.md) | [Grid](Mesh.md#Grid-classmethod) |
| [Ico Sphere](#nodes) | [Mesh](Mesh.md) | [IcoSphere](Mesh.md#IcoSphere-classmethod) |
| [Mesh Circle](#nodes) | [Mesh](Mesh.md) | [Circle](Mesh.md#Circle-classmethod) |
| [Mesh Line](#nodes) | [Mesh](Mesh.md) | [Line](Mesh.md#Line-classmethod) / [LineEndPoints](Mesh.md#LineEndPoints-classmethod) / [LineOffset](Mesh.md#LineOffset-classmethod) / [LineEndPointsResolution](Mesh.md#LineEndPointsResolution-classmethod) / [LineOffsetResolution](Mesh.md#LineOffsetResolution-classmethod) / |
| [UV Sphere](#nodes) | [Mesh](Mesh.md) | [Circle](Mesh.md#Circle-classmethod) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Point

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Distribute Points in Volume](#nodes) | [Volume](Volume.md) | - [distribute_points](Volume.md#distribute_points)<br>- [distribute_points_random](Volume.md#distribute_points_random)<br>- [distribute_points_grid](Volume.md#distribute_points_grid)|
| [Distribute Points on Faces](#nodes) | [Face](Face.md) | - [distribute_points_random](Face.md#distribute_points_random)<br>- [distribute_points_poisson](Face.md#distribute_points_poisson)|
|      | [Mesh](Mesh.md) | [distribute_points_on_faces](Mesh.md#distribute_points_on_faces) |
| [Points](#nodes) | [Points](Points.md) | [Points](Points.md#Points-classmethod) |
| [Points to Vertices](#nodes) | [CloudPoint](CloudPoint.md) | [to_vertices](CloudPoint.md#to_vertices) |
|      | [Points](Points.md) | [to_vertices](Points.md#to_vertices) |
| [Points to Volume](#nodes) | [Points](Points.md) | - [to_volume](Points.md#to_volume)<br>- [to_volume_size](Points.md#to_volume_size)<br>- [to_volume_amount](Points.md#to_volume_amount)|
| [Set Point Radius](#nodes) | [CloudPoint](CloudPoint.md) | [radius](CloudPoint.md#radius) |
|      | [Points](Points.md) | [set_point_radius](Points.md#set_point_radius) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Text

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Join Strings](#nodes) | [String](String.md) | [join](String.md#join) |
|      | [function](function.md) | [join_strings](function.md#join_strings) |
| [Replace String](#nodes) | [String](String.md) | [replace](String.md#replace) |
|      | [function](function.md) | [replace_string](function.md#replace_string) |
| [Slice String](#nodes) | [String](String.md) | [slice](String.md#slice) |
|      | [function](function.md) | [slice_string](function.md#slice_string) |
| [String Length](#nodes) | [String](String.md) | [length](String.md#length-property) |
|      | [function](function.md) | [string_length](function.md#string_length) |
| [String to Curves](#nodes) | [String](String.md) | [to_curves](String.md#to_curves) |
|      | [function](function.md) | [string_to_curves](function.md#string_to_curves) |
| [Value to String](#nodes) | [Float](Float.md) | [to_string](Float.md#to_string) |
|      | [Integer](Integer.md) | [to_string](Integer.md#to_string) |
|      | [function](function.md) | [value_to_string](function.md#value_to_string) |
| [Special Characters](#nodes) | [String](String.md) | - [LineBreak](String.md#LineBreak-staticmethod)<br>- [Tab](String.md#Tab-staticmethod)|

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Texture

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Brick Texture](#nodes) | [Texture](Texture.md) | [brick](Texture.md#brick-staticmethod) |
| [Checker Texture](#nodes) | [Texture](Texture.md) | [checker](Texture.md#checker-staticmethod) |
| [Gradient Texture](#nodes) | [Texture](Texture.md) | [gradient](Texture.md#gradient-staticmethod) / [gradient_linear](Texture.md#gradient_linear-staticmethod) / [gradient_quadratic](Texture.md#gradient_quadratic-staticmethod) / [gradient_easing](Texture.md#gradient_easing-staticmethod) / [gradient_diagonal](Texture.md#gradient_diagonal-staticmethod) / [gradient_spherical](Texture.md#gradient_spherical-staticmethod) / [gradient_quadratic_sphere](Texture.md#gradient_quadratic_sphere-staticmethod) / [gradient_radial](Texture.md#gradient_radial-staticmethod) / |
| [Image Texture](#nodes) | [Image](Image.md) | [texture](Image.md#texture) |
|      | [Texture](Texture.md) | [image](Texture.md#image-staticmethod) |
| [Magic Texture](#nodes) | [Texture](Texture.md) | [magic](Texture.md#magic-staticmethod) |
| [Musgrave Texture](#nodes) | [Texture](Texture.md) | [musgrave](Texture.md#musgrave-staticmethod) |
| [Noise Texture](#nodes) | [Texture](Texture.md) | [noise](Texture.md#noise-staticmethod) / [noise_1D](Texture.md#noise_1D-staticmethod) / [noise_2D](Texture.md#noise_2D-staticmethod) / [noise_3D](Texture.md#noise_3D-staticmethod) / [noise_4D](Texture.md#noise_4D-staticmethod) / |
| [Voronoi Texture](#nodes) | [Texture](Texture.md) | [voronoi](Texture.md#voronoi-staticmethod) / [voronoi_1D](Texture.md#voronoi_1D-staticmethod) / [voronoi_2D](Texture.md#voronoi_2D-staticmethod) / [voronoi_3D](Texture.md#voronoi_3D-staticmethod) / [voronoi_4D](Texture.md#voronoi_4D-staticmethod) / |
| [Wave Texture](#nodes) | [Texture](Texture.md) | [wave](Texture.md#wave-staticmethod) / [wave_bands](Texture.md#wave_bands-staticmethod) / [wave_rings](Texture.md#wave_rings-staticmethod) / [wave_bands_sine](Texture.md#wave_bands_sine-staticmethod) / [wave_bands_saw](Texture.md#wave_bands_saw-staticmethod) / [wave_bands_triangle](Texture.md#wave_bands_triangle-staticmethod) / [wave_rings_sine](Texture.md#wave_rings_sine-staticmethod) / [wave_rings_saw](Texture.md#wave_rings_saw-staticmethod) / [wave_rings_triangle](Texture.md#wave_rings_triangle-staticmethod) / |
| [White Noise Texture](#nodes) | [Texture](Texture.md) | [white_noise](Texture.md#white_noise-staticmethod) / [white_noise_1D](Texture.md#white_noise_1D-staticmethod) / [white_noise_2D](Texture.md#white_noise_2D-staticmethod) / [white_noise_3D](Texture.md#white_noise_3D-staticmethod) / [white_noise_4D](Texture.md#white_noise_4D-staticmethod) / |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Utilities

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Accumulate Field](#nodes) | [Domain](Domain.md) | [accumulate_field](Domain.md#accumulate_field) |
| [Align Euler to Vector](#nodes) | [Rotation](Rotation.md) | [align_to_vector](Rotation.md#align_to_vector) |
|      | [Vector](Vector.md) | [align_euler_to_vector](Vector.md#align_euler_to_vector) |
|      | [function](function.md) | [align_euler_to_vector](function.md#align_euler_to_vector) |
| [Boolean Math](#nodes) | [Boolean](Boolean.md) | [b_and](Boolean.md#b_and) / [b_or](Boolean.md#b_or) / [b_not](Boolean.md#b_not) / [nand](Boolean.md#nand) / [nor](Boolean.md#nor) / [xnor](Boolean.md#xnor) / [xor](Boolean.md#xor) / [imply](Boolean.md#imply) / [nimply](Boolean.md#nimply) / |
|      | [function](function.md) | [b_and](function.md#b_and) / [b_or](function.md#b_or) / [b_not](function.md#b_not) / [nand](function.md#nand) / [nor](function.md#nor) / [xnor](function.md#xnor) / [xor](function.md#xor) / [imply](function.md#imply) / [nimply](function.md#nimply) / |
| [Clamp](#nodes) | [Float](Float.md) | - [clamp](Float.md#clamp)<br>- [clamp_min_max](Float.md#clamp_min_max)<br>- [clamp_range](Float.md#clamp_range)|
|      | [function](function.md) | - [clamp](function.md#clamp)<br>- [clamp_min_max](function.md#clamp_min_max)<br>- [clamp_range](function.md#clamp_range)|
| [Compare](#nodes) | [Color](Color.md) | [compare](Color.md#compare) / [darker](Color.md#darker) / [brighter](Color.md#brighter) / [equal](Color.md#equal) / [equal](Color.md#equal) / |
|      | [Float](Float.md) | [compare](Float.md#compare) / [less_than](Float.md#less_than) / [less_equal](Float.md#less_equal) / [greater_than](Float.md#greater_than) / [greater_equal](Float.md#greater_equal) / [equal](Float.md#equal) / [not_equal](Float.md#not_equal) / |
|      | [Integer](Integer.md) | [compare](Integer.md#compare) / [less_than](Integer.md#less_than) / [less_equal](Integer.md#less_equal) / [greater_than](Integer.md#greater_than) / [greater_equal](Integer.md#greater_equal) / [equal](Integer.md#equal) / [not_equal](Integer.md#not_equal) / |
|      | [String](String.md) | - [equal](String.md#equal)<br>- [not_equal](String.md#not_equal)|
|      | [Vector](Vector.md) | [compare](Vector.md#compare) / [elements_less_than](Vector.md#elements_less_than) / [elements_less_equal](Vector.md#elements_less_equal) / [elements_greater_than](Vector.md#elements_greater_than) / [elements_greater_equal](Vector.md#elements_greater_equal) / [elements_equal](Vector.md#elements_equal) / [elements_not_equal](Vector.md#elements_not_equal) / [length_less_than](Vector.md#length_less_than) / [length_less_equal](Vector.md#length_less_equal) / [length_greater_than](Vector.md#length_greater_than) / [length_greater_equal](Vector.md#length_greater_equal) / [length_equal](Vector.md#length_equal) / [length_not_equal](Vector.md#length_not_equal) / [average_less_than](Vector.md#average_less_than) / [average_less_equal](Vector.md#average_less_equal) / [average_greater_than](Vector.md#average_greater_than) / [average_greater_equal](Vector.md#average_greater_equal) / [average_equal](Vector.md#average_equal) / [average_not_equal](Vector.md#average_not_equal) / [dot_product_less_than](Vector.md#dot_product_less_than) / [dot_product_less_equal](Vector.md#dot_product_less_equal) / [dot_product_greater_than](Vector.md#dot_product_greater_than) / [dot_product_greater_equal](Vector.md#dot_product_greater_equal) / [dot_product_equal](Vector.md#dot_product_equal) / [dot_product_not_equal](Vector.md#dot_product_not_equal) / [direction_less_than](Vector.md#direction_less_than) / [direction_less_equal](Vector.md#direction_less_equal) / [direction_greater_than](Vector.md#direction_greater_than) / [direction_greater_equal](Vector.md#direction_greater_equal) / [direction_equal](Vector.md#direction_equal) / [direction_not_equal](Vector.md#direction_not_equal) / |
|      | [function](function.md) | [compare](function.md#compare) |
| [Field at Index](#nodes) | [Domain](Domain.md) | [field_at_index](Domain.md#field_at_index) |
|      | [Geometry](Geometry.md) | [field_at_index](Geometry.md#field_at_index) |
| [Float Curve](#nodes) | [Float](Float.md) | [float_curve](Float.md#float_curve) |
| [Float to Integer](#nodes) | [Float](Float.md) | [to_integer](Float.md#to_integer) / [round](Float.md#round) / [floor](Float.md#floor) / [ceiling](Float.md#ceiling) / [truncate](Float.md#truncate) / |
| [Map Range](#nodes) | [Float](Float.md) | [map_range](Float.md#map_range) / [map_range_linear](Float.md#map_range_linear) / [map_range_stepped](Float.md#map_range_stepped) / [map_range_smooth](Float.md#map_range_smooth) / [map_range_smoother](Float.md#map_range_smoother) / |
|      | [Vector](Vector.md) | [map_range](Vector.md#map_range) / [map_range_linear](Vector.md#map_range_linear) / [map_range_stepped](Vector.md#map_range_stepped) / [map_range_smooth](Vector.md#map_range_smooth) / [map_range_smoother](Vector.md#map_range_smoother) / |
| [Math](#nodes) | [Float](Float.md) | [add](Float.md#add) / [subtract](Float.md#subtract) / [sub](Float.md#sub) / [multiply](Float.md#multiply) / [mul](Float.md#mul) / [divide](Float.md#divide) / [div](Float.md#div) / [multiply_add](Float.md#multiply_add) / [mul_add](Float.md#mul_add) / [power](Float.md#power) / [pow](Float.md#pow) / [logarithm](Float.md#logarithm) / [log](Float.md#log) / [sqrt](Float.md#sqrt) / [inverse_sqrt](Float.md#inverse_sqrt) / [absolute](Float.md#absolute) / [abs](Float.md#abs) / [exponent](Float.md#exponent) / [exp](Float.md#exp) / [minimum](Float.md#minimum) / [min](Float.md#min) / [maximum](Float.md#maximum) / [max](Float.md#max) / [math_less_than](Float.md#math_less_than) / [math_greater_than](Float.md#math_greater_than) / [sign](Float.md#sign) / [math_compare](Float.md#math_compare) / [smooth_minimum](Float.md#smooth_minimum) / [smooth_maximum](Float.md#smooth_maximum) / [math_round](Float.md#math_round) / [math_floor](Float.md#math_floor) / [math_ceil](Float.md#math_ceil) / [math_truncate](Float.md#math_truncate) / [math_trunc](Float.md#math_trunc) / [fraction](Float.md#fraction) / [fact](Float.md#fact) / [modulo](Float.md#modulo) / [wrap](Float.md#wrap) / [snap](Float.md#snap) / [ping_pong](Float.md#ping_pong) / [sine](Float.md#sine) / [sin](Float.md#sin) / [cosine](Float.md#cosine) / [cos](Float.md#cos) / [tangent](Float.md#tangent) / [tan](Float.md#tan) / [arcsine](Float.md#arcsine) / [arcsin](Float.md#arcsin) / [arccosine](Float.md#arccosine) / [arccos](Float.md#arccos) / [arctangent](Float.md#arctangent) / [arctan](Float.md#arctan) / [arctan2](Float.md#arctan2) / [sinh](Float.md#sinh) / [cosh](Float.md#cosh) / [tanh](Float.md#tanh) / [to_radians](Float.md#to_radians) / [to_degrees](Float.md#to_degrees) / |
|      | [Integer](Integer.md) | [add](Integer.md#add) / [subtract](Integer.md#subtract) / [sub](Integer.md#sub) / [multiply](Integer.md#multiply) / [mul](Integer.md#mul) / [divide](Integer.md#divide) / [div](Integer.md#div) / [multiply_add](Integer.md#multiply_add) / [mul_add](Integer.md#mul_add) / [power](Integer.md#power) / [pow](Integer.md#pow) / [logarithm](Integer.md#logarithm) / [log](Integer.md#log) / [sqrt](Integer.md#sqrt) / [inverse_sqrt](Integer.md#inverse_sqrt) / [absolute](Integer.md#absolute) / [abs](Integer.md#abs) / [exponent](Integer.md#exponent) / [exp](Integer.md#exp) / [minimum](Integer.md#minimum) / [min](Integer.md#min) / [maximum](Integer.md#maximum) / [max](Integer.md#max) / [math_less_than](Integer.md#math_less_than) / [math_greater_than](Integer.md#math_greater_than) / [sign](Integer.md#sign) / [math_compare](Integer.md#math_compare) / [smooth_minimum](Integer.md#smooth_minimum) / [smooth_maximum](Integer.md#smooth_maximum) / [math_round](Integer.md#math_round) / [math_floor](Integer.md#math_floor) / [math_ceil](Integer.md#math_ceil) / [math_truncate](Integer.md#math_truncate) / [math_trunc](Integer.md#math_trunc) / [fraction](Integer.md#fraction) / [fact](Integer.md#fact) / [modulo](Integer.md#modulo) / [wrap](Integer.md#wrap) / [snap](Integer.md#snap) / [ping_pong](Integer.md#ping_pong) / [sine](Integer.md#sine) / [sin](Integer.md#sin) / [cosine](Integer.md#cosine) / [cos](Integer.md#cos) / [tangent](Integer.md#tangent) / [tan](Integer.md#tan) / [arcsine](Integer.md#arcsine) / [arcsin](Integer.md#arcsin) / [arccosine](Integer.md#arccosine) / [arccos](Integer.md#arccos) / [arctangent](Integer.md#arctangent) / [arctan](Integer.md#arctan) / [arctan2](Integer.md#arctan2) / [sinh](Integer.md#sinh) / [cosh](Integer.md#cosh) / [tanh](Integer.md#tanh) / [to_radians](Integer.md#to_radians) / [to_degrees](Integer.md#to_degrees) / |
|      | [function](function.md) | [math](function.md#math) / [add](function.md#add) / [subtract](function.md#subtract) / [sub](function.md#sub) / [multiply](function.md#multiply) / [mul](function.md#mul) / [divide](function.md#divide) / [div](function.md#div) / [multiply_add](function.md#multiply_add) / [mul_add](function.md#mul_add) / [power](function.md#power) / [logarithm](function.md#logarithm) / [log](function.md#log) / [sqrt](function.md#sqrt) / [inverse_sqrt](function.md#inverse_sqrt) / [absolute](function.md#absolute) / [abs](function.md#abs) / [exponent](function.md#exponent) / [exp](function.md#exp) / [minimum](function.md#minimum) / [min](function.md#min) / [maximum](function.md#maximum) / [max](function.md#max) / [math_less_than](function.md#math_less_than) / [math_greater_than](function.md#math_greater_than) / [sign](function.md#sign) / [math_compare](function.md#math_compare) / [smooth_minimum](function.md#smooth_minimum) / [smooth_maximum](function.md#smooth_maximum) / [math_round](function.md#math_round) / [math_floor](function.md#math_floor) / [math_ceil](function.md#math_ceil) / [math_truncate](function.md#math_truncate) / [math_trun](function.md#math_trun) / [fraction](function.md#fraction) / [modulo](function.md#modulo) / [wrap](function.md#wrap) / [snap](function.md#snap) / [ping_pong](function.md#ping_pong) / [sine](function.md#sine) / [sin](function.md#sin) / [cosine](function.md#cosine) / [cos](function.md#cos) / [tangent](function.md#tangent) / [tan](function.md#tan) / [arcsine](function.md#arcsine) / [arcsin](function.md#arcsin) / [arccosine](function.md#arccosine) / [arccos](function.md#arccos) / [arctangent](function.md#arctangent) / [arctan](function.md#arctan) / [arctan2](function.md#arctan2) / [sinh](function.md#sinh) / [cosh](function.md#cosh) / [tanh](function.md#tanh) / [to_radians](function.md#to_radians) / [to_degrees](function.md#to_degrees) / |
| [Random Value](#nodes) | [Domain](Domain.md) | - [random_float](Domain.md#random_float)<br>- [random_integer](Domain.md#random_integer)<br>- [random_vector](Domain.md#random_vector)<br>- [random_boolean](Domain.md#random_boolean)|
|      | [Geometry](Geometry.md) | - [random_float](Geometry.md#random_float)<br>- [random_integer](Geometry.md#random_integer)<br>- [random_vector](Geometry.md#random_vector)<br>- [random_boolean](Geometry.md#random_boolean)|
|      | [function](function.md) | - [random_float](function.md#random_float)<br>- [random_integer](function.md#random_integer)<br>- [random_vector](function.md#random_vector)<br>- [random_boolean](function.md#random_boolean)|
| [Rotate Euler](#nodes) | [Rotation](Rotation.md) | - [Euler](Rotation.md#Euler-classmethod)<br>- [AxisAngle](Rotation.md#AxisAngle-classmethod)<br>- [rotate_euler](Rotation.md#rotate_euler)<br>- [rotate_axis_angle](Rotation.md#rotate_axis_angle)|
|      | [function](function.md) | - [rotate_euler](function.md#rotate_euler)<br>- [rotate_axis_angle](function.md#rotate_axis_angle)|
| [Switch](#nodes) | [Boolean](Boolean.md) | [switch](Boolean.md#switch) |
|      | [Collection](Collection.md) | [switch](Collection.md#switch) |
|      | [Color](Color.md) | [switch](Color.md#switch) |
|      | [Float](Float.md) | [switch](Float.md#switch) |
|      | [Geometry](Geometry.md) | [switch](Geometry.md#switch) |
|      | [Image](Image.md) | [switch](Image.md#switch) |
|      | [Integer](Integer.md) | [switch](Integer.md#switch) |
|      | [Material](Material.md) | [switch](Material.md#switch) |
|      | [Object](Object.md) | [switch](Object.md#switch) |
|      | [String](String.md) | [switch](String.md#switch) |
|      | [Texture](Texture.md) | [switch](Texture.md#switch) |
|      | [Vector](Vector.md) | [switch](Vector.md#switch) |
|      | [function](function.md) | [switch](function.md#switch) / [switch_float](function.md#switch_float) / [switch_integer](function.md#switch_integer) / [switch_boolean](function.md#switch_boolean) / [switch_vector](function.md#switch_vector) / [switch_string](function.md#switch_string) / [switch_color](function.md#switch_color) / [switch_object](function.md#switch_object) / [switch_image](function.md#switch_image) / [switch_geometry](function.md#switch_geometry) / [switch_collection](function.md#switch_collection) / [switch_texture](function.md#switch_texture) / [switch_material](function.md#switch_material) / |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu UV

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Pack UV Islands](#nodes) | [Face](Face.md) | [pack_uv_islands](Face.md#pack_uv_islands) |
|      | [Mesh](Mesh.md) | [pack_uv_islands](Mesh.md#pack_uv_islands) |
| [UV Unwrap](#nodes) | [Face](Face.md) | [uv_unwrap](Face.md#uv_unwrap) |
|      | [Mesh](Mesh.md) | [uv_unwrap](Mesh.md#uv_unwrap) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Vector

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Combine XYZ](#nodes) | [Vector](Vector.md) | [Combine](Vector.md#Combine-classmethod) |
| [Separate XYZ](#nodes) | [Vector](Vector.md) | [separate](Vector.md#separate-property) |
| [Vector Curves](#nodes) | [Vector](Vector.md) | [curves](Vector.md#curves) |
| [Vector Math](#nodes) | [Vector](Vector.md) | [add](Vector.md#add) / [subtract](Vector.md#subtract) / [sub](Vector.md#sub) / [multiply](Vector.md#multiply) / [mul](Vector.md#mul) / [divide](Vector.md#divide) / [div](Vector.md#div) / [multiply_add](Vector.md#multiply_add) / [mul_add](Vector.md#mul_add) / [cross_product](Vector.md#cross_product) / [cross](Vector.md#cross) / [project](Vector.md#project) / [reflect](Vector.md#reflect) / [refract](Vector.md#refract) / [face_forward](Vector.md#face_forward) / [dot_product](Vector.md#dot_product) / [dot](Vector.md#dot) / [distance](Vector.md#distance) / [length](Vector.md#length-property) / [scale](Vector.md#scale) / [normalize](Vector.md#normalize) / [absolute](Vector.md#absolute) / [abs](Vector.md#abs) / [minimum](Vector.md#minimum) / [min](Vector.md#min) / [maximum](Vector.md#maximum) / [max](Vector.md#max) / [floor](Vector.md#floor) / [ceil](Vector.md#ceil) / [fraction](Vector.md#fraction) / [fract](Vector.md#fract) / [modulo](Vector.md#modulo) / [wrap](Vector.md#wrap) / [snap](Vector.md#snap) / [sine](Vector.md#sine) / [sin](Vector.md#sin) / [cosine](Vector.md#cosine) / [cos](Vector.md#cos) / [tangent](Vector.md#tangent) / [tan](Vector.md#tan) / |
| [Vector Rotate](#nodes) | [Vector](Vector.md) | [rotate_euler](Vector.md#rotate_euler) / [rotate_axis_angle](Vector.md#rotate_axis_angle) / [rotate_x](Vector.md#rotate_x) / [rotate_y](Vector.md#rotate_y) / [rotate_z](Vector.md#rotate_z) / |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Volume

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Volume Cube](#nodes) | [Volume](Volume.md) | [Cube](Volume.md#Cube-classmethod) |
| [Volume to Mesh](#nodes) | [Volume](Volume.md) | [to_mesh](Volume.md#to_mesh) |

<sub>Go to [top](#nodes-menus) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>
