import unittest
import src.cq_examples.Ex001_Simple_Block as ex

class TestExample001(unittest.TestCase):
	def test_Ex001(self):
		# Import and validate
		R = ex.result
		self.assertTrue(R.val().isValid())

		# Volume calculation
		length = ex.length
		height = ex.height
		thickness = ex.thickness
		vol = length * height * thickness
		self.assertEqual(R.val().Volume(), vol)
