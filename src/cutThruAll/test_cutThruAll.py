import unittest

class TestCutThruAll(unittest.TestCase):

    # Import and validate C1
    def test_C1(self):
        import src.cutThruAll.C1
        global R1
        R1 = src.cutThruAll.C1.result
        self.assertTrue(R1.val().isValid())

    # Import and validate C2
    def test_C2(self):
        import src.cutThruAll.C2
        global R2
        R2 = src.cutThruAll.C2.result
        self.assertTrue(R2.val().isValid())

    # Tests if the objects are equal
    def test_equal(self):
        self.assertAlmostEqual(R1.cut(R2).val().Volume(), 0)
        self.assertAlmostEqual(R1.union(R2).val().Volume(), R1.val().Volume())
        self.assertAlmostEqual(R1.intersect(R2).val().Volume(), R1.val().Volume())
