import cadquery as cq

r = 3 # Radius of the helix
p = 1.5 # Pitch of the helix
h = 4 # Height of the helix

# Helix
wire = cq.Wire.makeHelix(pitch=p, height=h, radius=r)
shape = cq.Wire.combine([wire])
helix = cq.Workplane("XY").newObject([shape])

# Final result. A circle sweeped along a helix.
result = (
    cq.Workplane('XZ')
    .center(r, 0)
    .circle(0.1)
    .sweep(helix, isFrenet=True)
)
