import unittest
import cq_examples.Ex005_Extruded_Lines_and_Arcs as ex

class TestExample005(unittest.TestCase):
	def test_Ex005(self):
		# Import and validate
		R = ex.result
		self.assertTrue(R.val().isValid())