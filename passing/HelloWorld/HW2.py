import cadquery as cq

result = cq.Workplane().rect(3, 4, centered=False).extrude(1)
