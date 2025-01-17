from geonodes import nodes
import geonodes as gn

with gn.Tree('Geometry Nodes') as tree:

    boolean    = gn.Boolean()
    integer    = gn.Integer()
    float      = gn.Float()
    vector     = gn.Vector()
    color      = gn.Color()
    string     = gn.String()
    texture    = gn.Texture.Input()
    image      = gn.Image.Input()
    material   = gn.Material.Input()
    collection = gn.Collection.Input()
    object     = gn.Object.Input()
    geometry   = tree.ig
    mesh       = gn.Mesh.Cube()
    curve      = gn.Curve.Circle()
    points     = gn.Points.Points()
    instances  = gn.Instances.InstanceOnPoints(points=points)
    volume     = gn.Volume.Cube()

    geometry.attribute_statistic()
    geometry.capture_attribute()
    var = gn.Geometry.capture_attribute_node()
    var = geometry.domain_size
    geometry.store_named_attribute()
    geometry.store_named_boolean()
    geometry.store_named_integer()
    geometry.store_named_float()
    geometry.store_named_vector()
    geometry.store_named_color()
    geometry.remove_named_attribute()
    var = geometry.bounding_box
    var = geometry.bounding_box_min
    var = geometry.bounding_box_min
    var = geometry.convex_hull
    geometry.delete()
    geometry.duplicate()
    geometry.proximity()
    geometry.proximity_points()
    geometry.proximity_edges()
    geometry.proximity_faces()
    geometry.to_instance()
    geometry.join()
    geometry.merge_by_distance()
    geometry.raycast()
    geometry.raycast_interpolated()
    geometry.raycast_nearest()
    geometry.sample_index()
    geometry.sample_nearest()
    var = geometry.separate_components
    var = geometry.mesh_component
    var = geometry.curve_component
    var = geometry.points_component
    var = geometry.volume_component
    var = geometry.instances_component
    geometry.separate()
    geometry.transform()
    geometry.set_ID()
    geometry.set_position()
    var = gn.Geometry.Collection()
    var = geometry.is_viewport
    var = geometry.ID
    var = geometry.index
    geometry.named_attribute()
    geometry.named_float()
    geometry.named_integer()
    geometry.named_vector()
    geometry.named_color()
    geometry.named_boolean()
    var = geometry.normal
    var = geometry.position
    var = geometry.radius
    geometry.replace_material()
    var = geometry.material_index
    geometry.material_selection()
    geometry.set_material()
    geometry.set_material_index()
    geometry.viewer()
    geometry.view()
    geometry.field_at_index()
    geometry.interpolate_domain()
    var = gn.Geometry.random_float()
    var = gn.Geometry.random_integer()
    var = gn.Geometry.random_vector()
    var = gn.Geometry.random_boolean()
    geometry.switch()
    mesh.verts.attribute_statistic()
    mesh.edges.attribute_statistic()
    mesh.faces.attribute_statistic()
    mesh.corners.attribute_statistic()
    curve.points.attribute_statistic()
    curve.splines.attribute_statistic()
    instances.insts.attribute_statistic()
    points.points.attribute_statistic()
    mesh.verts.attribute_mean()
    mesh.edges.attribute_mean()
    mesh.faces.attribute_mean()
    mesh.corners.attribute_mean()
    curve.points.attribute_mean()
    curve.splines.attribute_mean()
    instances.insts.attribute_mean()
    points.points.attribute_mean()
    mesh.verts.attribute_median()
    mesh.edges.attribute_median()
    mesh.faces.attribute_median()
    mesh.corners.attribute_median()
    curve.points.attribute_median()
    curve.splines.attribute_median()
    instances.insts.attribute_median()
    points.points.attribute_median()
    mesh.verts.attribute_sum()
    mesh.edges.attribute_sum()
    mesh.faces.attribute_sum()
    mesh.corners.attribute_sum()
    curve.points.attribute_sum()
    curve.splines.attribute_sum()
    instances.insts.attribute_sum()
    points.points.attribute_sum()
    mesh.verts.attribute_min()
    mesh.edges.attribute_min()
    mesh.faces.attribute_min()
    mesh.corners.attribute_min()
    curve.points.attribute_min()
    curve.splines.attribute_min()
    instances.insts.attribute_min()
    points.points.attribute_min()
    mesh.verts.attribute_max()
    mesh.edges.attribute_max()
    mesh.faces.attribute_max()
    mesh.corners.attribute_max()
    curve.points.attribute_max()
    curve.splines.attribute_max()
    instances.insts.attribute_max()
    points.points.attribute_max()
    mesh.verts.attribute_range()
    mesh.edges.attribute_range()
    mesh.faces.attribute_range()
    mesh.corners.attribute_range()
    curve.points.attribute_range()
    curve.splines.attribute_range()
    instances.insts.attribute_range()
    points.points.attribute_range()
    mesh.verts.attribute_std()
    mesh.edges.attribute_std()
    mesh.faces.attribute_std()
    mesh.corners.attribute_std()
    curve.points.attribute_std()
    curve.splines.attribute_std()
    instances.insts.attribute_std()
    points.points.attribute_std()
    mesh.verts.attribute_var()
    mesh.edges.attribute_var()
    mesh.faces.attribute_var()
    mesh.corners.attribute_var()
    curve.points.attribute_var()
    curve.splines.attribute_var()
    instances.insts.attribute_var()
    points.points.attribute_var()
    mesh.verts.capture_attribute()
    mesh.edges.capture_attribute()
    mesh.faces.capture_attribute()
    mesh.corners.capture_attribute()
    curve.points.capture_attribute()
    curve.splines.capture_attribute()
    instances.insts.capture_attribute()
    points.points.capture_attribute()
    mesh.verts.store_named_attribute_no_selection()
    mesh.edges.store_named_attribute_no_selection()
    mesh.faces.store_named_attribute_no_selection()
    mesh.corners.store_named_attribute_no_selection()
    curve.points.store_named_attribute_no_selection()
    curve.splines.store_named_attribute_no_selection()
    instances.insts.store_named_attribute_no_selection()
    points.points.store_named_attribute_no_selection()
    mesh.verts.remove_named_attribute()
    mesh.edges.remove_named_attribute()
    mesh.faces.remove_named_attribute()
    mesh.corners.remove_named_attribute()
    curve.points.remove_named_attribute()
    curve.splines.remove_named_attribute()
    instances.insts.remove_named_attribute()
    points.points.remove_named_attribute()
    mesh.verts.sample_index()
    mesh.edges.sample_index()
    mesh.faces.sample_index()
    mesh.corners.sample_index()
    curve.points.sample_index()
    curve.splines.sample_index()
    instances.insts.sample_index()
    points.points.sample_index()
    mesh.verts.set_ID()
    mesh.edges.set_ID()
    mesh.faces.set_ID()
    mesh.corners.set_ID()
    curve.points.set_ID()
    curve.splines.set_ID()
    instances.insts.set_ID()
    points.points.set_ID()
    mesh.verts.ID = None
    mesh.edges.ID = None
    mesh.faces.ID = None
    mesh.corners.ID = None
    curve.points.ID = None
    curve.splines.ID = None
    instances.insts.ID = None
    points.points.ID = None
    mesh.verts.set_position()
    mesh.edges.set_position()
    mesh.faces.set_position()
    mesh.corners.set_position()
    curve.points.set_position()
    curve.splines.set_position()
    instances.insts.set_position()
    points.points.set_position()
    mesh.verts.position = None
    mesh.edges.position = None
    mesh.faces.position = None
    mesh.corners.position = None
    curve.points.position = None
    curve.splines.position = None
    instances.insts.position = None
    points.points.position = None
    var = mesh.verts.ID
    var = mesh.edges.ID
    var = mesh.faces.ID
    var = mesh.corners.ID
    var = curve.points.ID
    var = curve.splines.ID
    var = instances.insts.ID
    var = points.points.ID
    var = mesh.verts.index
    var = mesh.edges.index
    var = mesh.faces.index
    var = mesh.corners.index
    var = curve.points.index
    var = curve.splines.index
    var = instances.insts.index
    var = points.points.index
    var = mesh.verts.domain_index
    var = mesh.edges.domain_index
    var = mesh.faces.domain_index
    var = mesh.corners.domain_index
    var = curve.points.domain_index
    var = curve.splines.domain_index
    var = instances.insts.domain_index
    var = points.points.domain_index
    mesh.verts.named_attribute()
    mesh.edges.named_attribute()
    mesh.faces.named_attribute()
    mesh.corners.named_attribute()
    curve.points.named_attribute()
    curve.splines.named_attribute()
    instances.insts.named_attribute()
    points.points.named_attribute()
    mesh.verts.named_float()
    mesh.edges.named_float()
    mesh.faces.named_float()
    mesh.corners.named_float()
    curve.points.named_float()
    curve.splines.named_float()
    instances.insts.named_float()
    points.points.named_float()
    mesh.verts.named_integer()
    mesh.edges.named_integer()
    mesh.faces.named_integer()
    mesh.corners.named_integer()
    curve.points.named_integer()
    curve.splines.named_integer()
    instances.insts.named_integer()
    points.points.named_integer()
    mesh.verts.named_vector()
    mesh.edges.named_vector()
    mesh.faces.named_vector()
    mesh.corners.named_vector()
    curve.points.named_vector()
    curve.splines.named_vector()
    instances.insts.named_vector()
    points.points.named_vector()
    mesh.verts.named_color()
    mesh.edges.named_color()
    mesh.faces.named_color()
    mesh.corners.named_color()
    curve.points.named_color()
    curve.splines.named_color()
    instances.insts.named_color()
    points.points.named_color()
    mesh.verts.named_boolean()
    mesh.edges.named_boolean()
    mesh.faces.named_boolean()
    mesh.corners.named_boolean()
    curve.points.named_boolean()
    curve.splines.named_boolean()
    instances.insts.named_boolean()
    points.points.named_boolean()
    var = mesh.verts.normal
    var = mesh.edges.normal
    var = mesh.faces.normal
    var = mesh.corners.normal
    var = curve.points.normal
    var = curve.splines.normal
    var = instances.insts.normal
    var = points.points.normal
    var = mesh.verts.position
    var = mesh.edges.position
    var = mesh.faces.position
    var = mesh.corners.position
    var = curve.points.position
    var = curve.splines.position
    var = instances.insts.position
    var = points.points.position
    mesh.verts.material_selection()
    mesh.edges.material_selection()
    mesh.faces.material_selection()
    mesh.corners.material_selection()
    curve.points.material_selection()
    curve.splines.material_selection()
    instances.insts.material_selection()
    points.points.material_selection()
    mesh.verts.viewer()
    mesh.edges.viewer()
    mesh.faces.viewer()
    mesh.corners.viewer()
    curve.points.viewer()
    curve.splines.viewer()
    instances.insts.viewer()
    points.points.viewer()
    mesh.verts.view()
    mesh.edges.view()
    mesh.faces.view()
    mesh.corners.view()
    curve.points.view()
    curve.splines.view()
    instances.insts.view()
    points.points.view()
    mesh.verts.accumulate_field()
    mesh.edges.accumulate_field()
    mesh.faces.accumulate_field()
    mesh.corners.accumulate_field()
    curve.points.accumulate_field()
    curve.splines.accumulate_field()
    instances.insts.accumulate_field()
    points.points.accumulate_field()
    mesh.verts.field_at_index()
    mesh.edges.field_at_index()
    mesh.faces.field_at_index()
    mesh.corners.field_at_index()
    curve.points.field_at_index()
    curve.splines.field_at_index()
    instances.insts.field_at_index()
    points.points.field_at_index()
    mesh.verts.interpolate()
    mesh.edges.interpolate()
    mesh.faces.interpolate()
    mesh.corners.interpolate()
    curve.points.interpolate()
    curve.splines.interpolate()
    instances.insts.interpolate()
    points.points.interpolate()
    var = gn.Domain.random_float()
    var = gn.Domain.random_float()
    var = gn.Domain.random_float()
    var = gn.Domain.random_float()
    var = gn.Domain.random_float()
    var = gn.Domain.random_float()
    var = gn.Domain.random_float()
    var = gn.Domain.random_float()
    var = gn.Domain.random_integer()
    var = gn.Domain.random_integer()
    var = gn.Domain.random_integer()
    var = gn.Domain.random_integer()
    var = gn.Domain.random_integer()
    var = gn.Domain.random_integer()
    var = gn.Domain.random_integer()
    var = gn.Domain.random_integer()
    var = gn.Domain.random_vector()
    var = gn.Domain.random_vector()
    var = gn.Domain.random_vector()
    var = gn.Domain.random_vector()
    var = gn.Domain.random_vector()
    var = gn.Domain.random_vector()
    var = gn.Domain.random_vector()
    var = gn.Domain.random_vector()
    var = gn.Domain.random_boolean()
    var = gn.Domain.random_boolean()
    var = gn.Domain.random_boolean()
    var = gn.Domain.random_boolean()
    var = gn.Domain.random_boolean()
    var = gn.Domain.random_boolean()
    var = gn.Domain.random_boolean()
    var = gn.Domain.random_boolean()
    var = mesh.domain_size
    var = mesh.point_count
    var = mesh.face_count
    var = mesh.edge_count
    var = mesh.corner_count
    mesh.delete_all()
    mesh.delete_edges()
    mesh.delete_faces()
    mesh.instance_on_points()
    mesh.dual_mesh()
    mesh.edge_paths_to_curves()
    mesh.edge_paths_to_selection()
    mesh.extrude()
    mesh.flip_faces()
    mesh.boolean_intersect()
    mesh.boolean_union()
    mesh.boolean_difference()
    mesh.to_curve()
    mesh.to_points()
    mesh.to_volume()
    mesh.sample_nearest_surface()
    mesh.sample_uv_surface()
    mesh.scale_elements()
    mesh.scale_uniform()
    mesh.scale_single_axis()
    mesh.split_edges()
    mesh.subdivide()
    mesh.subdivision_surface()
    mesh.triangulate()
    mesh.face_set_boundaries()
    mesh.face_is_planar()
    mesh.is_shade_smooth()
    var = mesh.island
    var = mesh.island_index
    var = mesh.island_count
    mesh.shortest_edge_paths()
    mesh.set_shade_smooth()
    var = gn.Mesh.Cone()
    var = gn.Mesh.Cube()
    var = gn.Mesh.Cylinder()
    var = gn.Mesh.Grid()
    var = gn.Mesh.IcoSphere()
    var = gn.Mesh.Circle()
    var = gn.Mesh.Line()
    var = gn.Mesh.LineEndPoints()
    var = gn.Mesh.LineEndPointsResolution()
    var = gn.Mesh.LineOffset()
    var = gn.Mesh.UVSphere()
    mesh.corners_of_face()
    mesh.corners_of_vertex()
    mesh.edges_of_corner()
    mesh.edges_of_vertex()
    mesh.face_of_corner()
    mesh.offset_corner_in_face()
    mesh.vertex_of_corner()
    mesh.distribute_points_on_faces()
    mesh.pack_uv_islands()
    mesh.uv_unwrap()
    var = curve.domain_size
    var = curve.point_count
    var = curve.spline_count
    var = curve.length
    curve.to_mesh()
    curve.to_points()
    curve.to_points_count()
    curve.to_points_length()
    curve.to_points_evaluated()
    curve.deform_on_surface()
    curve.fill()
    curve.fill_triangles()
    curve.fill_ngons()
    curve.fillet()
    curve.fillet_bezier()
    curve.fillet_poly()
    curve.resample()
    curve.resample_count()
    curve.resample_length()
    curve.resample_evaluated()
    curve.reverse()
    curve.sample()
    curve.subdivide()
    curve.trim()
    curve.trim_factor()
    curve.trim_length()
    var = gn.Curve.Arc()
    var = gn.Curve.ArcFromPoints()
    var = gn.Curve.BezierSegment()
    var = gn.Curve.Circle()
    var = gn.Curve.CircleFromPoints()
    var = gn.Curve.Line()
    var = gn.Curve.LineDirection()
    var = gn.Curve.Spiral()
    var = gn.Curve.QuadraticBezier()
    var = gn.Curve.Quadrilateral()
    var = gn.Curve.Star()
    curve.offset_point()
    curve.curve_of_point()
    curve.points_of_curve()
    curve.instance_on_points()
    var = points.domain_size
    points.instance_on_points()
    var = gn.Points.Points()
    points.to_vertices()
    points.to_volume()
    points.to_volume_size()
    points.to_volume_amount()
    points.set_point_radius()
    var = instances.domain_size
    var = gn.Instances.InstanceOnPoints()
    instances.on_points()
    instances.to_points()
    instances.realize()
    instances.rotate()
    instances.set_scale()
    instances.translate()
    var = instances.scale
    var = instances.rotation
    var = mesh.verts.count
    mesh.verts.delete()
    mesh.verts.delete_all()
    mesh.verts.delete_edges()
    mesh.verts.delete_faces()
    mesh.verts.duplicate()
    mesh.verts.proximity()
    mesh.verts.merge_by_distance()
    mesh.verts.merge_by_distance_connected()
    mesh.verts.sample_nearest()
    mesh.verts.separate()
    mesh.verts.instance_on_points()
    mesh.verts.extrude()
    mesh.verts.to_points()
    mesh.verts.to_volume()
    var = mesh.verts.neighbors
    var = mesh.verts.neighbors_vertex_count
    var = mesh.verts.neighbors_face_count
    mesh.verts.corners()
    mesh.verts.corners_index()
    mesh.verts.corners_total()
    mesh.verts.edges()
    mesh.verts.edges_index()
    mesh.verts.edges_total()
    var = mesh.faces.count
    mesh.faces.delete()
    mesh.faces.delete_all()
    mesh.faces.delete_edges()
    mesh.faces.delete_faces()
    mesh.faces.duplicate()
    mesh.faces.proximity()
    mesh.faces.sample_nearest()
    mesh.faces.separate()
    var = mesh.faces.material_index
    mesh.faces.set_material()
    
    mesh.faces.material = None
    mesh.faces.set_material_index()
    mesh.faces.material_index = None
    mesh.faces.extrude()
    mesh.faces.flip()
    mesh.faces.scale_uniform()
    mesh.faces.scale_single_axis()
    mesh.faces.triangulate()
    var = mesh.faces.area
    var = mesh.faces.neighbors
    var = mesh.faces.neighbors_vertex_count
    var = mesh.faces.neighbors_face_count
    mesh.faces.face_set_boundaries()
    mesh.faces.is_planar()
    var = mesh.faces.shade_smooth
    var = mesh.faces.island
    var = mesh.faces.island_index
    var = mesh.faces.island_count
    mesh.faces.set_shade_smooth()
    mesh.faces.shade_smooth = None
    mesh.faces.corners()
    mesh.faces.corners_index()
    mesh.faces.corners_total()
    mesh.faces.distribute_points_random()
    mesh.faces.distribute_points_poisson()
    mesh.faces.pack_uv_islands()
    mesh.faces.uv_unwrap()
    var = mesh.edges.count
    mesh.edges.delete()
    mesh.edges.delete_all()
    mesh.edges.delete_edges()
    mesh.edges.delete_faces()
    mesh.edges.duplicate()
    mesh.edges.proximity()
    mesh.edges.sample_nearest()
    mesh.edges.separate()
    mesh.edges.edge_paths_to_curves()
    mesh.edges.extrude()
    mesh.edges.to_curve()
    mesh.edges.scale_uniform()
    mesh.edges.scale_single_axis()
    mesh.edges.split()
    var = mesh.edges.angle
    var = mesh.edges.unsigned_angle
    var = mesh.edges.signed_angle
    var = mesh.edges.neighbors
    var = mesh.edges.vertices
    var = mesh.edges.vertices_index
    var = mesh.edges.vertices_position
    var = mesh.corners.count
    mesh.corners.sample_nearest()
    mesh.corners.edges()
    var = mesh.corners.previous_vertex
    var = mesh.corners.next_vertex
    mesh.corners.face()
    var = mesh.corners.face_index
    var = mesh.corners.index_in_face
    mesh.corners.offset_in_face()
    var = mesh.corners.vertex_index
    var = curve.splines.count
    curve.splines.resample()
    curve.splines.resample_count()
    curve.splines.resample_length()
    curve.splines.resample_evaluated()
    var = curve.splines.cyclic
    var = curve.splines.length
    var = curve.splines.resolution
    curve.splines.set_normal()
    curve.splines.normal = 'MINIMUM_TWIST'
    curve.splines.set_cyclic()
    curve.splines.cyclic = None
    curve.splines.set_resolution()
    curve.splines.resolution = None
    curve.splines.set_type()
    
    curve.splines.type = 'POLY'
    curve.splines.points()
    curve.splines.delete()
    curve.splines.duplicate()
    curve.splines.separate()
    var = curve.splines.normal
    var = curve.splines.material_index
    curve.splines.set_material()
    
    curve.splines.material = None
    curve.splines.set_material_index()
    curve.splines.material_index = None
    var = curve.points.count
    curve.points.handle_positions()
    var = curve.points.left_handle_positions
    var = curve.points.right_handle_positions
    var = curve.points.tangent
    var = curve.points.tilt
    curve.points.endpoint_selection()
    curve.points.handle_type_selection_node()
    curve.points.handle_type_selection()
    curve.points.handle_type_selection()
    curve.points.handle_type_selection()
    curve.points.handle_type_selection()
    curve.points.handle_type_selection()
    var = curve.points.parameter
    var = curve.points.parameter_factor
    var = curve.points.parameter_length
    var = curve.points.parameter_index
    curve.points.set_radius()
    curve.points.radius = None
    curve.points.set_tilt()
    curve.points.tilt = None
    curve.points.set_handle_positions()
    curve.points.set_handle_positions_left()
    curve.points.set_handle_positions_right()
    curve.points.left_handle_positions = (1, 2, 3)
    curve.points.right_handle_positions = (1, 2, 3)
    curve.points.set_handle_type_node()
    curve.points.set_handle_type()
    curve.points.offset()
    curve.points.curve()
    curve.points.delete()
    curve.points.duplicate()
    curve.points.proximity()
    curve.points.separate()
    var = curve.points.radius
    curve.points.instance_on_points()
    var = points.points.count
    points.points.delete()
    points.points.duplicate()
    points.points.proximity()
    var = points.points.radius
    points.points.instance_on_points()
    points.points.to_vertices()
    points.points.radius = None
    var = instances.insts.count
    instances.insts.delete()
    instances.insts.duplicate()
    instances.insts.separate()
    instances.insts.to_points()
    instances.insts.rotate()
    instances.insts.set_scale()
    instances.insts.translate()
    var = instances.insts.scale
    var = instances.insts.rotation
    gn.color_ramp()
    gn.combine_rgb()
    gn.combine_hsv()
    gn.combine_hsl()
    gn.float_mix()
    gn.vector_mix()
    gn.color_mix()
    gn.color_darken()
    gn.color_multiply()
    gn.color_burn()
    gn.color_lighten()
    gn.color_screen()
    gn.color_dodge()
    gn.color_add()
    gn.color_overlay()
    gn.color_soft_light()
    gn.color_linear_light()
    gn.color_difference()
    gn.color_subtract()
    gn.color_divide()
    gn.color_hue()
    gn.color_saturation()
    gn.color_color()
    gn.color_value()
    gn.rgb_curves()
    gn.separate_rgb()
    gn.separate_hsv()
    gn.separate_hsl()
    gn.geometry_to_instance()
    gn.join_geometry()
    gn.join_strings()
    gn.replace_string()
    gn.slice_string()
    gn.string_length()
    gn.string_to_curves()
    gn.value_to_string()
    gn.align_euler_to_vector()
    gn.b_and()
    gn.b_or()
    gn.b_not()
    gn.nand()
    gn.nor()
    gn.xnor()
    gn.xor()
    gn.imply()
    gn.nimply()
    gn.clamp()
    gn.clamp_min_max()
    gn.clamp_range()
    gn.compare()
    gn.math()
    gn.multiply_add()
    gn.mul_add()
    gn.power()
    gn.logarithm()
    gn.log()
    gn.sqrt()
    gn.inverse_sqrt()
    gn.absolute()
    gn.abs()
    gn.exponent()
    gn.exp()
    gn.minimum()
    gn.min()
    gn.maximum()
    gn.max()
    gn.math_less_than()
    gn.math_greater_than()
    gn.sign()
    gn.math_compare()
    gn.smooth_minimum()
    gn.smooth_maximum()
    gn.math_round()
    gn.math_floor()
    gn.math_ceil()
    gn.math_truncate()
    gn.math_trun()
    gn.fraction()
    gn.modulo()
    gn.wrap()
    gn.snap()
    gn.ping_pong()
    gn.sine()
    gn.sin()
    gn.cosine()
    gn.cos()
    gn.tangent()
    gn.tan()
    gn.arcsine()
    gn.arcsin()
    gn.arccosine()
    gn.arccos()
    gn.arctangent()
    gn.arctan()
    gn.arctan2()
    gn.sinh()
    gn.cosh()
    gn.tanh()
    gn.to_radians()
    gn.to_degrees()
    gn.random_float()
    gn.random_integer()
    gn.random_vector()
    gn.random_boolean()
    gn.rotate_euler()
    gn.rotate_axis_angle()
    gn.switch()
    gn.switch_float()
    gn.switch_integer()
    gn.switch_boolean()
    gn.switch_vector()
    gn.switch_string()
    gn.switch_color()
    gn.switch_object()
    gn.switch_image()
    gn.switch_geometry()
    gn.switch_collection()
    gn.switch_texture()
    gn.switch_material()
    var = float.color_ramp
    float.mix()
    var = gn.Float.Value()
    var = gn.Float.Seconds()
    var = gn.Float.Frame()
    float.to_string()
    float.clamp()
    float.clamp_min_max()
    float.clamp_range()
    float.compare()
    float.less_than()
    float.less_equal()
    float.greater_than()
    float.greater_equal()
    float.equal()
    float.not_equal()
    float.float_curve()
    float.to_integer()
    float.round()
    float.floor()
    float.ceiling()
    float.truncate()
    float.map_range()
    float.map_range_linear()
    float.map_range_stepped()
    float.map_range_smooth()
    float.map_range_smoother()
    float.multiply_add()
    float.mul_add()
    float.power()
    float.pow()
    float.logarithm()
    float.log()
    float.sqrt()
    float.inverse_sqrt()
    float.absolute()
    float.abs()
    float.exponent()
    float.exp()
    float.minimum()
    float.min()
    float.maximum()
    float.max()
    float.math_less_than()
    float.math_greater_than()
    float.sign()
    float.math_compare()
    float.smooth_minimum()
    float.smooth_maximum()
    float.math_round()
    float.math_floor()
    float.math_ceil()
    float.math_truncate()
    float.math_trunc()
    float.fraction()
    float.fact()
    float.modulo()
    float.wrap()
    float.snap()
    float.ping_pong()
    float.sine()
    float.sin()
    float.cosine()
    float.cos()
    float.tangent()
    float.tan()
    float.arcsine()
    float.arcsin()
    float.arccosine()
    float.arccos()
    float.arctangent()
    float.arctan()
    float.arctan2()
    float.sinh()
    float.cosh()
    float.tanh()
    float.to_radians()
    float.to_degrees()
    var = gn.Float.Random()
    float.switch()
    var = gn.Color.RGB()
    var = gn.Color.HSV()
    var = gn.Color.HSL()
    color.mix()
    color.mix_darken()
    color.mix_multiply()
    color.mix_burn()
    color.mix_lighten()
    color.mix_screen()
    color.mix_dodge()
    color.mix_add()
    color.mix_overlay()
    color.mix_soft_light()
    color.mix_linear_light()
    color.mix_difference()
    color.mix_subtract()
    color.mix_divide()
    color.mix_hue()
    color.mix_saturation()
    color.mix_color()
    color.mix_value()
    var = color.rgb_curves
    color.separate_color()
    var = gn.Color.Color()
    color.darker()
    color.brighter()
    color.equal()
    color.equal()
    color.switch()
    vector.mix()
    vector.mix_uniform()
    vector.mix_non_uniform()
    var = gn.Vector.Vector()
    vector.align_euler_to_vector()
    var = gn.Vector.AlignToVector()
    vector.compare()
    vector.elements_less_than()
    vector.elements_less_equal()
    vector.elements_greater_than()
    vector.elements_greater_equal()
    vector.elements_equal()
    vector.elements_not_equal()
    vector.length_less_than()
    vector.length_less_equal()
    vector.length_greater_than()
    vector.length_greater_equal()
    vector.length_equal()
    vector.length_not_equal()
    vector.average_less_than()
    vector.average_less_equal()
    vector.average_greater_than()
    vector.average_greater_equal()
    vector.average_equal()
    vector.average_not_equal()
    vector.dot_product_less_than()
    vector.dot_product_less_equal()
    vector.dot_product_greater_than()
    vector.dot_product_greater_equal()
    vector.dot_product_equal()
    vector.dot_product_not_equal()
    vector.direction_less_than()
    vector.direction_less_equal()
    vector.direction_greater_than()
    vector.direction_greater_equal()
    vector.direction_equal()
    vector.direction_not_equal()
    vector.map_range()
    vector.map_range_linear()
    vector.map_range_stepped()
    vector.map_range_smooth()
    vector.map_range_smoother()
    var = gn.Vector.Random()
    vector.switch()
    var = gn.Vector.Combine()
    var = vector.separate
    vector.curves()
    vector.add()
    vector.subtract()
    vector.sub()
    vector.multiply()
    vector.mul()
    vector.divide()
    vector.div()
    vector.multiply_add()
    vector.mul_add()
    vector.cross_product()
    vector.cross()
    vector.project()
    vector.reflect()
    vector.refract()
    vector.face_forward()
    vector.dot_product()
    vector.dot()
    vector.distance()
    var = vector.length
    vector.scale()
    vector.normalize()
    vector.absolute()
    vector.abs()
    vector.minimum()
    vector.min()
    vector.maximum()
    vector.max()
    vector.floor()
    vector.ceil()
    vector.fraction()
    vector.fract()
    vector.modulo()
    vector.wrap()
    vector.snap()
    vector.sine()
    vector.sin()
    vector.cosine()
    vector.cos()
    vector.tangent()
    vector.tan()
    vector.rotate_euler()
    vector.rotate_axis_angle()
    vector.rotate_x()
    vector.rotate_y()
    vector.rotate_z()
    var = gn.Boolean.Boolean()
    boolean.b_and()
    boolean.b_or()
    boolean.b_not()
    boolean.nand()
    boolean.nor()
    boolean.xnor()
    boolean.xor()
    boolean.imply()
    boolean.nimply()
    var = gn.Boolean.Random()
    boolean.switch()
    var = gn.Integer.Integer()
    integer.to_string()
    integer.compare()
    integer.less_than()
    integer.less_equal()
    integer.greater_than()
    integer.greater_equal()
    integer.equal()
    integer.not_equal()
    integer.multiply_add()
    integer.mul_add()
    integer.power()
    integer.pow()
    integer.logarithm()
    integer.log()
    integer.sqrt()
    integer.inverse_sqrt()
    integer.absolute()
    integer.abs()
    integer.exponent()
    integer.exp()
    integer.minimum()
    integer.min()
    integer.maximum()
    integer.max()
    integer.math_less_than()
    integer.math_greater_than()
    integer.sign()
    integer.math_compare()
    integer.smooth_minimum()
    integer.smooth_maximum()
    integer.math_round()
    integer.math_floor()
    integer.math_ceil()
    integer.math_truncate()
    integer.math_trunc()
    integer.fraction()
    integer.fact()
    integer.modulo()
    integer.wrap()
    integer.snap()
    integer.ping_pong()
    integer.sine()
    integer.sin()
    integer.cosine()
    integer.cos()
    integer.tangent()
    integer.tan()
    integer.arcsine()
    integer.arcsin()
    integer.arccosine()
    integer.arccos()
    integer.arctangent()
    integer.arctan()
    integer.arctan2()
    integer.sinh()
    integer.cosh()
    integer.tanh()
    integer.to_radians()
    integer.to_degrees()
    var = gn.Integer.Random()
    integer.switch()
    var = gn.Material.Material()
    material.switch()
    object.info()
    object.location()
    object.rotation()
    object.scale()
    object.geometry()
    var = gn.Object.Self()
    object.switch()
    var = gn.String.String()
    string.join()
    string.string_join()
    string.replace()
    string.slice()
    var = string.length
    string.to_curves()
    var = gn.String.LineBreak()
    var = gn.String.Tab()
    string.equal()
    string.not_equal()
    string.switch()
    volume.distribute_points()
    volume.distribute_points_random()
    volume.distribute_points_grid()
    var = gn.Volume.Cube()
    volume.to_mesh()
    var = gn.Texture.brick()
    var = gn.Texture.checker()
    var = gn.Texture.gradient()
    var = gn.Texture.gradient_linear()
    var = gn.Texture.gradient_quadratic()
    var = gn.Texture.gradient_easing()
    var = gn.Texture.gradient_diagonal()
    var = gn.Texture.gradient_spherical()
    var = gn.Texture.gradient_quadratic_sphere()
    var = gn.Texture.gradient_radial()
    var = gn.Texture.image()
    var = gn.Texture.magic()
    var = gn.Texture.musgrave()
    var = gn.Texture.noise()
    var = gn.Texture.noise_1D()
    var = gn.Texture.noise_2D()
    var = gn.Texture.noise_3D()
    var = gn.Texture.noise_4D()
    var = gn.Texture.voronoi()
    var = gn.Texture.voronoi_1D()
    var = gn.Texture.voronoi_2D()
    var = gn.Texture.voronoi_3D()
    var = gn.Texture.voronoi_4D()
    var = gn.Texture.wave()
    var = gn.Texture.wave_bands()
    var = gn.Texture.wave_rings()
    var = gn.Texture.wave_bands_sine()
    var = gn.Texture.wave_bands_saw()
    var = gn.Texture.wave_bands_triangle()
    var = gn.Texture.wave_rings_sine()
    var = gn.Texture.wave_rings_saw()
    var = gn.Texture.wave_rings_triangle()
    var = gn.Texture.white_noise()
    var = gn.Texture.white_noise_1D()
    var = gn.Texture.white_noise_2D()
    var = gn.Texture.white_noise_3D()
    var = gn.Texture.white_noise_4D()
    texture.switch()
    image.texture()
    image.switch()
    collection.switch()

    tree.og = geometry

