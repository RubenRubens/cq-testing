import unittest
import cq_examples.Ex021_Splitting_an_Object as ex

class TestExample021(unittest.TestCase):
    def test_Ex021(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
