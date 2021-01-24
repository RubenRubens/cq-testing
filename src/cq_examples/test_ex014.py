import unittest
import src.cq_examples.Ex014_Offset_Workplanes as ex

class TestExample014(unittest.TestCase):
    def test_Ex014(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
