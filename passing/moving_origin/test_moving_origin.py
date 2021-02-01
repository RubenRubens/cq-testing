import unittest

class TestMovingOrigin(unittest.TestCase):

    # Import and validate M1
    def test_M1(self):
        import moving_origin.M1
        global R1
        R1 = moving_origin.M1.result
        self.assertTrue(R1.val().isValid())

    # Import and validate M2
    def test_M2(self):
        import moving_origin.M2
        global R2
        R2 = moving_origin.M2.result
        self.assertTrue(R2.val().isValid())

    # Tests if the objects are equal
    def test_equal(self):
        self.assertAlmostEqual(R1.cut(R2).val().Volume(), 0)
        self.assertAlmostEqual(R1.union(R2).val().Volume(), R1.val().Volume())
        self.assertAlmostEqual(R1.intersect(R2).val().Volume(), R1.val().Volume())
