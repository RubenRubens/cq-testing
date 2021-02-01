import unittest

class TestHelloWorld(unittest.TestCase):

    # Import and validate HW1
    def test_HW1(self):
        import HelloWorld.HW1
        global R1
        R1 = HelloWorld.HW1.result
        self.assertTrue(R1.val().isValid())

    # Import and validate HW2
    def test_HW2(self):
        import HelloWorld.HW2
        global R2
        R2 = HelloWorld.HW2.result
        self.assertTrue(R2.val().isValid())

    # Tests if the objects are equal
    def test_equal(self):
        self.assertEqual(R1.cut(R2).val().Volume(), 0)
        self.assertEqual(R1.union(R2).val().Volume(), R1.val().Volume())
        self.assertEqual(R1.intersect(R2).val().Volume(), R1.val().Volume())
