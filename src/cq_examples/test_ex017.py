import unittest
import src.cq_examples.Ex017_Shelling_to_Create_Thin_Features as ex

class TestExample017(unittest.TestCase):
    def test_Ex017(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
