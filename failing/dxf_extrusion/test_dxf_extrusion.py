import unittest

class TestDXFextrusion(unittest.TestCase):

    # Import and validate A1
    def test_A1(self):
        import dxf_extrusion.A1
        global R1
        R1 = dxf_extrusion.A1.result
        self.assertTrue(R1.val().isValid())

    # Import and validate A2
    def test_A2(self):
        import dxf_extrusion.A2
        global R2
        R2 = dxf_extrusion.A2.result
        self.assertTrue(R2.val().isValid())

    # Tests if the objects are equal
    def test_equal(self):
        self.assertEqual(R1.cut(R2).val().Volume(), 0)
        self.assertEqual(R1.union(R2).val().Volume(), R1.val().Volume())
        self.assertEqual(R1.intersect(R2).val().Volume(), R1.val().Volume())
