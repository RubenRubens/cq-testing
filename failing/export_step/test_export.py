# issue 697

import cadquery as cq
import unittest


def create_geometry():

    widget = cq.Workplane("XY").rect(5, 5).extrude(0.5)

    oddly_shaped_holes = (
        cq.Workplane("XY")
        .move(0, 1.2)
        .lineTo(-0.5, 1.2)
        .lineTo(-0.5, 1.5)
        .lineTo(-1.5, 1.5)
        .lineTo(-1.5, 0)
        .mirrorX()
        .mirrorY()
        .extrude(2)
        .edges("|Z")
        .fillet(0.13)
    )

    bunch_of_cylinders = (
        cq.Workplane("XY")
        .rarray(1, 3, 4, 2)
        .eachpoint(
            lambda loc: cq.Workplane("XY").circle(0.15).extrude(2).val().located(loc)
        )
    )
    widget = widget.cut(oddly_shaped_holes)
    widget = widget.cut(bunch_of_cylinders)

    cq.exporters.export(widget, f"export_step/widget.step")

    return widget


class TestExportStep(unittest.TestCase):
    def test_equality(self):
        native = create_geometry()
        step = cq.importers.importStep("export_step/widget.step")

        self.assertAlmostEqual(native.cut(step).val().Volume(), 0, places=2)
        self.assertAlmostEqual(native.union(step).val().Volume(), native.val().Volume(), places=2)
        self.assertAlmostEqual(native.intersect(step).val().Volume(), native.val().Volume(), places=2)
