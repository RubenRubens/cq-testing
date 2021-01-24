import unittest
import src.cq_examples.Ex024_Sweep_With_Multiple_Sections as ex

class TestExample024(unittest.TestCase):
    def test_Ex024(self):
        # Import and validate
        self.assertTrue(ex.a.val().isValid())
        self.assertTrue(ex.b.val().isValid())
        self.assertTrue(ex.c.val().isValid())
        self.assertTrue(ex.d.val().isValid())
        self.assertTrue(ex.e.val().isValid())
