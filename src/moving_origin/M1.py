# issue 577

import cadquery as cq

# The issue are these two lines
solid = cq.Workplane("XZ").moveTo(50, 0).workplane(centerOption="CenterOfMass")
solid = solid.polyline([(-10, 10), (10, 10), (10, -10), (-10, -10)]).close()

result = solid.extrude(1)
