import unittest
import cq_examples.Ex019_Counter_Sunk_Holes as ex

class TestExample019(unittest.TestCase):
    def test_Ex019(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
