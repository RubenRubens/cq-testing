import unittest
import cq_examples.Ex100_Lego_Brick as ex

class TestExample100(unittest.TestCase):
    def test_Ex100(self):
        # Import and validate
        R = ex.tmp
        self.assertTrue(R.val().isValid())
