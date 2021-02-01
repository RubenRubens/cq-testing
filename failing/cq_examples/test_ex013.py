import unittest
import cq_examples.Ex013_Locating_a_Workplane_on_a_Vertex as ex

class TestExample013(unittest.TestCase):
    def test_Ex013(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
