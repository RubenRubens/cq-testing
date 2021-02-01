import unittest
import cq_examples.Ex015_Rotated_Workplanes as ex

class TestExample015(unittest.TestCase):
    def test_Ex015(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
