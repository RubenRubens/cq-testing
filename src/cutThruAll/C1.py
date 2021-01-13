# issue 355

import cadquery as cq

sphere_r = 10.

result = (cq.Workplane("XY").sphere(sphere_r)
            .workplane(centerOption="ProjectedOrigin").circle(sphere_r / 2.).cutThruAll()
            .workplane(centerOption="ProjectedOrigin").transformed(rotate=(90, 0, 0))
            .circle(sphere_r / 2.).cutThruAll()
            .workplane(centerOption="ProjectedOrigin").transformed(rotate=(0, 90, 0))
            .circle(sphere_r / 2.).cutThruAll()
            .workplane(centerOption="ProjectedOrigin").circle(sphere_r / 2.).extrude(sphere_r + 2, both=True))
