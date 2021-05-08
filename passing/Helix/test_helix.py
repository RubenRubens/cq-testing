import cadquery as cq
import unittest
from math import pi, cos, sin


def A():
    r = 3 # Radius of the helix
    p = 1.5 # Pitch of the helix
    h = 4 # Height of the helix

    # Helix
    wire = cq.Wire.makeHelix(pitch=p, height=h, radius=r)
    helix = cq.Workplane(obj=wire)

    # Final result. A circle sweeped along a helix.
    result = (
        cq.Workplane('XZ')
        .center(r, 0)
        .circle(0.1)
        .sweep(helix, isFrenet=True)
    )

    return result


def B():
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

    return result


class TestHelix(unittest.TestCase):
    def test_volumes(self):
        R1 = A()
        R2 = B()
        self.assertAlmostEqual(R1.cut(R2).val().Volume(), 0, places=4)
        self.assertAlmostEqual(R1.union(R2).val().Volume(), R1.val().Volume(), places=4)
        self.assertAlmostEqual(R1.intersect(R2).val().Volume(), R1.val().Volume(), places=4)