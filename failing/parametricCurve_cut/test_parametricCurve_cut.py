# issue 260

import cadquery as cq
import unittest
from math import pi, cos, sin


def A():
    # the base body
    s = cq.Workplane('XY').circle(50).extrude(20)
    
    # this will be cut away
    to_cut = (
        cq.Workplane('XY')
        .transformed(offset=[35,0,0], rotate=[90,0,0])
        .circle(14)
        .revolve(315, [-35,0,0], [-35,1,0])
    )
    
    return s.cut(to_cut)


def B():
    s = cq.Workplane('XY').circle(50).extrude(20)
    
    def my_ellipse(t, a, b):
        return (a*sin(2*pi*t), b*cos(2*pi*t))

    to_cut = (
        cq.Workplane('XY')
        .transformed(offset=[35,0,0], rotate=[90,0,0])
        .parametricCurve(lambda t: my_ellipse(t,14,7))
        .revolve(315, [-35,0,0], [-35,1,0])
    )

    return s.cut(to_cut)


class TestHelix(unittest.TestCase):
    def test_volumes(self):
        R1 = A()
        R2 = B()
        self.assertTrue(R1.val().isValid())
        self.assertTrue(R2.val().isValid())
        self.assertAlmostEqual(R1.cut(R2).val().Volume(), 0, places=3)
        self.assertAlmostEqual(R1.union(R2).val().Volume(), R1.val().Volume(), places=3)
        self.assertAlmostEqual(R1.intersect(R2).val().Volume(), R1.val().Volume(), places=3)