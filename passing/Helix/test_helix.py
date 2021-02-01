import unittest

class TestHelix(unittest.TestCase):

    # Import and validate H1
    def test_H1(self):
        import Helix.H1
        global R1
        R1 = Helix.H1.result
        self.assertTrue(R1.val().isValid())

    # Import and validate H2
    def test_H2(self):
        import Helix.H2
        global R2
        R2 = Helix.H2.result
        self.assertTrue(R2.val().isValid())

    # Tests if the objects are equal
    def test_equal(self):
        self.assertAlmostEqual(R1.cut(R2).val().Volume(), 0, places=4)
        self.assertAlmostEqual(R1.union(R2).val().Volume(), R1.val().Volume(), places=4)
        self.assertAlmostEqual(R1.intersect(R2).val().Volume(), R1.val().Volume(), places=4)
