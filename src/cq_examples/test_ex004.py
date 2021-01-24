import unittest
from math import pi
import src.cq_examples.Ex004_Extruded_Cylindrical_Plate as ex

class TestExample004(unittest.TestCase):
	def test_Ex004(self):
		# Import and validate
		circle_radius = ex.circle_radius
		thickness = ex.thickness
		rectangle_width = ex.rectangle_width
		rectangle_length = ex.rectangle_length
		R = ex.result
		self.assertTrue(R.val().isValid())

		# Check volume
		vol = pi * circle_radius**2 * thickness
		vol -= rectangle_width * rectangle_length * thickness
		self.assertAlmostEqual(R.val().Volume(), vol)
