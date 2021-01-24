import unittest
import src.cq_examples.Ex023_Sweep as ex

class TestExample023(unittest.TestCase):
    def test_Ex023(self):
        # Import and validate
        self.assertTrue(ex.a.val().isValid())
        self.assertTrue(ex.b.val().isValid())
        self.assertTrue(ex.c.val().isValid())
        self.assertTrue(ex.d.val().isValid())
        self.assertTrue(ex.e.val().isValid())
