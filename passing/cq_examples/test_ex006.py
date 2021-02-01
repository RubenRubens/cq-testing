import unittest
from math import pi
import cq_examples.Ex006_Moving_the_Current_Working_Point as ex

class TestExample006(unittest.TestCase):
	def test_Ex006(self):
		# Import and validate
		R = ex.result
		self.assertTrue(R.val().isValid())

		# Check volume
		circle_radius = ex.circle_radius
		thickness = ex.thickness
		vol = (pi * circle_radius**2 - pi * 0.25**2 - 0.5**2) * thickness
		self.assertAlmostEqual(R.val().Volume(), vol)
