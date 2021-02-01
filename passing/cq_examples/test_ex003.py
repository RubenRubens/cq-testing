import unittest
from math import pi
import cq_examples.Ex003_Pillow_Block_With_Counterbored_Holes as ex

class TestExample003(unittest.TestCase):
	def test_Ex003(self):
		# Import and validate
		length = ex.length
		width = ex.width
		thickness = ex.thickness
		center_hole_dia = ex.center_hole_dia
		cbore_hole_diameter = ex.cbore_hole_diameter
		cbore_inset = ex.cbore_inset
		cbore_diameter = ex.cbore_diameter
		cbore_depth = ex.cbore_depth
		R = ex.result
		self.assertTrue(R.val().isValid())

		# Volume calculation
		vol = length * width * thickness
		vol -= pi * (center_hole_dia/2)**2 * thickness
		vol -= 4 * pi * (cbore_hole_diameter/2)**2 * (thickness-cbore_depth)
		vol -= 4 * pi * (cbore_diameter/2)**2 * cbore_depth
		vol -= (4**2 - pi * 2**2) * thickness
		self.assertAlmostEqual(R.val().Volume(), vol)
