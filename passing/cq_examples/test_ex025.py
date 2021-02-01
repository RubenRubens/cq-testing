import unittest
import cq_examples.Ex025_Swept_Helix as ex

class TestExample025(unittest.TestCase):
    def test_Ex025(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
