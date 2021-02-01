import unittest
import cq_examples.Ex020_Rounding_Corners_with_Fillets as ex

class TestExample020(unittest.TestCase):
    def test_Ex020(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
