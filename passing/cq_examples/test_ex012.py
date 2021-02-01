import unittest
import cq_examples.Ex012_Creating_Workplanes_on_Faces as ex

class TestExample012(unittest.TestCase):
    def test_Ex012(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
