import cadquery as cq
from math import sin, cos, pi

r = 3 # Radius of the helix
p = 1.5 # Pitch of the helix
h = 4 # Height of the helix

# Helix
helix = cq.Workplane('XY').parametricCurve(
    lambda t : (
        r * cos(t * 2 * pi),
        r * sin(t * 2 * pi),
        p * t
    ),
    start=0,
    stop=h/p
)

# Final result. A circle sweeped along a helix.
result = (
    cq.Workplane('XZ')
    .center(r, 0)
    .circle(0.1)
    .sweep(helix, isFrenet=True)
)
