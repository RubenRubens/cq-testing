import unittest
from math import pi
import cq_examples.Ex002_Block_With_Bored_Center_Hole as ex

class TestExample002(unittest.TestCase):
	def test_Ex002(self):
		# Import and validate
		R = ex.result
		self.assertTrue(R.val().isValid())
		
		# Volume calculation
		length = ex.length
		height = ex.height
		thickness = ex.thickness
		r = ex.center_hole_dia / 2
		vol = length * height * thickness - r**2 * pi * thickness
		self.assertAlmostEqual(R.val().Volume(), vol)
