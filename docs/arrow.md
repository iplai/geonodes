# Building an arrow

> Tutorial on how to build a full parametrized arrow.

## Objective

We need arrows of different resolution, appearance, size which can take various orientations.
We want to control these parameters with the modifier, including the material on shaft and arrowhead.

The image below shows what we want to build:

<img src="_static/images/arrow_1.png" width="600" class="center">


## Parameters

The parameters to create are the following:

| Name             | Type           | Description                                                      |
| ---------------- | -------------- | ---------------------------------------------------------------- |
| Length           | Float          | Total length of the arrow, including the arrowhead               |
| Radius           | Float          | Radius shaft                                                     |
| Head size        | Float          | Size of the arrow head, expressed as a factor applied to radius  |
| Head angle       | Float (Angle)  | Angle of the arrowhead peak                                      |
| Recess           | Float          | How "deep" the shaft penetrates in the arrowhead (0: flat, 1: max) |
| Vertices         | Integer        | Circular resolution expressed inf number of vertices             |

We will add complementatry parameters later on but for the moment, these parameters allow to build the arrow.
The good practice is to start by declaring the parameters at the begining of the tree.

``` python
import numpy as np
import geonodes as gn

with gn.Tree("Arrow") as tree:

    length    = gn.Float.Input(1, "Length", min_value=0)
    r         = gn.Float.Input(0.1, "Radius", min_value=0.001)
    s         = gn.Float.Input(2, "Head size", min_value=1.001)
    angle     = gn.Float.Angle(np.radians(20), "Angle", min_value=np.radians(10), max_value=0.999*gn.pi/2)
    k         = gn.Float.Input(0.5, "Recess", min_value=0., max_value=0.99)
    vertices  = gn.Integer.Input(12, "Vertices", min_value=3)

```

## Some maths

We will build the arrow by extruding a base disk up along the z axis and then enlarging the cylinder to build the arrowhead.
Some maths are required to build the arrow according the parameters.

<img src="_static/images/Arrow_comp.png" width="600" class="center">

The corresponding python code is given here after:

``` python

    # ----- Arrowhead radius from the shaft radius

    rh = r*s

    # ----- Arrowhead height from the angle

    tg = gn.tan(angle)
    hh = rh/tg
    z0 = length - hh

    # ----- Recess computation

    h  = r/tg
    d  = k*h*(s - 1)

    z1 = z0 + d
    z2 = z0 + k*h*s
```

## Building by extrusion

The starting point is a disk:

``` python
    arrow = gn.Mesh.Circle(vertices=vertices, radius=r, fill_type='NGON')
```

The shaft length was computed above, it is equal to `z1`. Hence, the shaft is built by extruding the disk edges up to z1:

``` python
    edges = arrow.edges
    top, _ = edges.extrude(offset=(0, 0, 1), offset_scale=z1)
```

The extrude method returns two Boolean selections. The first one is the selection the extruded edges and the seconde one a selection
on the side faces. The faces are useless for now. In the final version we will set material to the faces and we will collect the faces.

The next extrusion step is to extrude the edges downwards and outwards.
It the scheme above, we are at points `Q'` and want to extrude to point `Q''`.
The direction of extrusion is given by the vector `QQ'`.
The amount of extrusion is given by the maths.

**Note:** Points `Q'` and  `Q''` are multiple (points forming the top circle of the shaft) when the point `Q` is unique.

``` python
    top, _ = edges[top].extrude(offset=edges[top].position - (0, 0, z2), offset_scale=s - 1)
```

To finish the arrow, we simply extrude from the current position to the top of the arrow:

``` python
    top, _ = edges[top].extrude(offset=(0, 0, length) - edges[top].position)
```

## First version

The first version of our arrow is then the following:

``` python
import numpy as np
import geonodes as gn

with gn.Tree("Arrow") as tree:

    length    = gn.Float.Input(1, "Length", min_value=0)
    r         = gn.Float.Input(0.1, "Radius", min_value=0.001)
    s         = gn.Float.Input(2, "Head size", min_value=1.001)
    angle     = gn.Float.Angle(np.radians(20), "Angle", min_value=np.radians(10), max_value=0.999*gn.pi/2)
    k         = gn.Float.Input(0.5, "Recess", min_value=0., max_value=0.99)
    vertices  = gn.Integer.Input(12, "Vertices", min_value=3)


    with tree.layout("Maths stuff..."):

        # ----- Arrowhead radius from the shaft radius

        rh = r*s

        # ----- Arrowhead height from the angle

        tg = gn.tan(angle)
        hh = rh/tg
        z0 = length - hh

        # ----- Recess computation

        h  = r/tg
        d  = k*h*(s - 1)

        z1 = z0 + d
        z2 = z0 + k*h*s

    # -----Extrusion

    arrow = gn.Mesh.Circle(vertices=vertices, radius=r, fill_type='NGON')
    edges = arrow.edges
    
    top, _ = edges.extrude(offset=(0, 0, 1), offset_scale=z1)
    
    top, _ = edges[top].extrude(offset=edges[top].position - (0, 0, z2), offset_scale=s - 1)

    top, _ = edges[top].extrude(offset=(0, 0, length) - edges[top].position)

    # ----- Output the arrow
    
    tree.og = arrow

```

## Edges and vertices position

The arrow looks good but a problem appears with low numbers of vertices: the vertices don't join at the top of the arrowhead.
For instance, with 5 vertices, the arrow is given below:

<img src="_static/images/arrow_2.png" width="600" class="center">

This is due to the fact that we extrude edges using their position.
The edges positions are supposed to be on a circle, when in reality, the edges positions are the mean of their two vertices.
The vertices are on the circle, when the edges position is within the circle.
Extrusion is instructed on edges but operated on vertices.
The position of the vertices is deducted from the positions of the two edges they are part of.
This computed position is even more inside the disk.

To correct that, we have to correct the edges positions with a factor computed from the number of vertices.
Without detailling the maths, the correction is the following:

``` python

    # ----- polygon correction factor
    # Extrusion uses edge position which is the mean of the two
    # extremities. The vertices position is then computed as the mean
    # of the two edges. Twice a cosine factor

    f = 1/gn.cos(gn.pi/vertices)**2
    fac = gn.Vector((f, f, 1))
     
        
```

And then:

``` python

    top, _ = edges[top].extrude(offset=edges[top].position*fac - (0, 0, z2), offset_scale=s - 1)

    top, _ = edges[top].extrude(offset=(0, 0, length) - edges[top].position*fac)

```

## Materials

We want to apply materials: one for the shaft and one for the rest.

Material is a property of faces, then we modify the code to:

- Get the materials as input
- Get the extruded faces
- Setting the material to the faces

``` python

    # Materials to apply

    shaft_mat = gn.Material.Input(None, "Shaft")
    head_mat  = gn.Material.Input(None, "Arrowhead")
    
    # ...
    
    arrow = gn.Mesh.Circle(vertices=vertices, radius=r, fill_type='NGON')
    
    # Apply the material to the base disk
    
    arrow.faces.material = head_mat

    # Applying material to extruded faces
    
    top, sides = arrow.edges.extrude(offset=(0, 0, 1), offset_scale=z1)
    arrow.faces[sides].material = shaft_mat

    top, sides = edges[top].extrude(offset=edges[top].position*fac - (0, 0, z2), offset_scale=s - 1)
    arrow.faces[sides].material = head_mat

    top, sides = edges[top].extrude(offset=(0, 0, length) - edges[top].position*fac)

```

## Arrow orientation

We want to orient our arrow. The orientation can be either the copy of the orientation of a reference object,
or the tracking of a target object.

We need to add an object plus a Boolean option to indicate how to use this object:

``` python
    obj       = gn.Object.Input(None, "Orientation")
    track_obj = gn.Boolean.Input(True, "Track", description="Track object if True, copy rotation otherwise")
```

In standard python, we would use a `if` statement.
But here, we need to compute both orientations and use a `switch` node:

``` python
    rot_copy  = obj.rotation(transform_space='ORIGINAL')
    loc       = obj.location(transform_space='RELATIVE')
    rot_track = gn.Vector.AlignToVector(vector=loc, axis='Z')

    arrow.transform(rotation=rot_copy.switch(track_obj, rot_track))
``` 

## The final arrow

The final code includes a smoothing option.

**Note:** One may want to add a _Subdivision surface_ modifier to the arrow.
To get a good result, we must add a crease property equal to 1 to "horizontal" edges.
But at the time this tuto is written, their is a known bug ([T99310](https://developer.blender.org/T99310)) in Blender which crashes when you try to set the attribute named "crease".
The code is given by using "waiting" name rather than "crease".

``` python
import numpy as np
import geonodes as gn

def arrow():
    
    with gn.Tree("Arrow") as tree:
        
        length    = gn.Float.Input(1, "Length", min_value=0)
        r         = gn.Float.Input(0.1, "Radius", min_value=0.001)
        s         = gn.Float.Input(2, "Head size", min_value=1.001)
        angle     = gn.Float.Angle(np.radians(20), "Angle", min_value=np.radians(10), max_value=0.999*gn.pi/2)
        k         = gn.Float.Input(0.5, "Recess", min_value=0., max_value=0.99)
        vertices  = gn.Integer.Input(12, "Vertices", min_value=3)
        smooth    = gn.Boolean.Input(True, "Shade smooth")
        shaft_mat = gn.Material.Input(None, "Shaft")
        head_mat  = gn.Material.Input(None, "Arrowhead")
        obj       = gn.Object.Input(None, "Orientation")
        track_obj = gn.Boolean.Input(True, "Track", description="Track object if True, copy rotation otherwise")
        
        with tree.layout("Maths stuff..."):
            
            # ----- Arrowhead radius from the shaft radius
            
            rh = r*s
            
            # ----- Arrowhead height from the angle

            tg = gn.tan(angle)
            hh = rh/tg
            z0 = length - hh
            
            # ----- Recess computation
            
            h  = r/tg
            d  = k*h*(s - 1)
            
            z1 = z0 + d
            z2 = z0 + k*h*s
            
            # ----- polygon correction factor
            # Extrusion uses edge position which is the mean of the two
            # extremities. The vertices position is then computed as the mean
            # of the two edges. Twice a cosine factor
            
            f = 1/gn.cos(gn.pi/vertices)**2
            fac = gn.Vector((f, f, 1))
            
        # ----- Let's go
        
        with tree.layout("Arrow base"):
        
            arrow = gn.Mesh.Circle(vertices=vertices, radius=r, fill_type='NGON')
            arrow.faces.material = head_mat
            
        with tree.layout("Extrusion"):
            
            edges = arrow.edges
            
            top, sides = edges.extrude(offset=(0, 0, 1), offset_scale=z1)
            arrow.faces[sides].material = shaft_mat
            
            top, sides = edges[top].extrude(offset=edges[top].position*fac - (0, 0, z2), offset_scale=s - 1)
            arrow.faces[sides].material = head_mat

            top, sides = edges[top].extrude(offset=(0, 0, length) - edges[top].position*fac)
            
        # ----- Set creae to 1 for horizontal edges
        
        # In current Blender version, crash when trying to set crease named attribute
        
        with tree.layout("crease and smoothing"):
        
            crease = "waiting"
                          
            p1, p2 = arrow.edges.vertices_position
            hrz = (p1.z - p2.z).abs().less_than(0.001)
            arrow.edges.set_named_float(crease, gn.Float(0).switch(hrz, 1))
            
            # ----- One point at the top
            
            arrow.faces.shade_smooth = smooth
            
        # ----- Orientation

        with tree.layout("Orientation"):
        
            rot_copy  = obj.rotation(transform_space='ORIGINAL')
            loc       = obj.location(transform_space='RELATIVE')
            rot_track = gn.Vector.AlignToVector(vector=loc, axis='Z')
            
            arrow.transform(rotation=rot_copy.switch(track_obj, rot_track))
    
        # ----- Done
        
        tree.og = arrow
        
arrow()
```






