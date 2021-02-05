import cadquery as cq

# Loft using 3 sketches
result = (
    cq.Workplane().ellipse(200/2, 150/2)
    .workplane(offset=50).ellipse(170/2, 115/2)
    .workplane(offset=30).circle(50)
    .loft()
)
