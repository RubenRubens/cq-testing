import unittest
import src.cq_examples.Ex009_Polylines as ex

class TestExample009(unittest.TestCase):
    def test_Ex009(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
