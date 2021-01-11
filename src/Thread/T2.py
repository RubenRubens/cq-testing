# Pach of H1

import cadquery as cq
from math import sin, cos, tan, pi

# Parameters
d = 10
p = 1.50
m = 8.10

# Constant
H = 0.866 * p

def spring():
    # Helix
    helix = cq.Workplane('XY', origin=(0,0,-1)).parametricCurve(
        lambda t : (
            d/2 * cos(t * 2 * pi),
            d/2 * sin(t * 2 * pi),
            p * t
        ),
        start = 0,
        stop = m/p
    )

    # Face
    face = cq.Workplane('XZ').center(d/2, 0).circle(0.3)

    return face.sweep(helix, isFrenet=True)

result = cq.Workplane().circle(d/2*1.4).circle(d/2*1).extrude(m).cut(spring())
