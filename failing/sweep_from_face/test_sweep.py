# issue 277

import cadquery as cq
import unittest


# This works as expected
def A():
    PDI = 4
    PDO = 8
    PDL = 20
    path = cq.Workplane("YZ").moveTo(0, PDL / 3).lineTo(0, 2 * PDL / 3)
    port = (
        cq.Workplane("XY")
        .workplane(offset=PDL / 3)
        .circle(PDO / 2)
        .workplane(offset=PDL / 3)
        .circle(PDI / 2)
        .sweep(path, multisection=True)
    )
    return port


# This does not
def B():
    PDI = 4
    PDO = 8
    PDL = 20
    s_shell = cq.Workplane("XY").box(8, 122, 62)
    port = s_shell.faces(">Z").circle(PDO / 2).extrude(PDL / 3)
    path = cq.Workplane("YZ").moveTo(0, PDL / 3).lineTo(0, 2 * PDL / 3)
    port = (
        port.faces(">Z")
        .workplane()
        .circle(PDO / 2)
        .workplane(offset=PDL / 3)
        .circle(PDI / 2)
        .sweep(path, multisection=True)
    )
    return port


class TestSweep(unittest.TestCase):
    def test_volumes(self):
        a = A()
        b = B()
        self.assertAlmostEqual(a.Volume(), b.Volume())
        self.assertAlmostEqual((a - b).Volume(), 0)
        self.assertAlmostEqual((b - a).Volume(), 0)