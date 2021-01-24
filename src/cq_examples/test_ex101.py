import unittest
import src.cq_examples.Ex101_InterpPlate as ex

class TestExample101(unittest.TestCase):
    def test_Ex101(self):
        # Import and validate
        plate_0 = ex.plate_0
        plate_1 = ex.plate_1
        plate_2 = ex.plate_2
        plate_3 = ex.plate_3
        plate_4 = ex.plate_4
        self.assertTrue(plate_0.val().isValid())
        self.assertTrue(plate_1.val().isValid())
        self.assertTrue(plate_2.val().isValid())
        self.assertTrue(plate_3.val().isValid())
        self.assertTrue(plate_4.val().isValid())
