import unittest

class TestHelix(unittest.TestCase):

	# Import and validate H1
	def test_H1(self):
		import src.Helix.H1
		global R1
		R1 = src.Helix.H1.result
		self.assertTrue(R1.val().isValid())

	# Import and validate H2
	def test_H2(self):
		import src.Helix.H2
		global R2
		R2 = src.Helix.H2.result
		self.assertTrue(R2.val().isValid())

	# Tests if the objects are equal
	def test_equal(self):
		self.assertEqual(R1.cut(R2).val().Volume(), 0)
		self.assertEqual(R1.union(R2).val().Volume(), R1.val().Volume())
		self.assertEqual(R1.intersect(R2).val().Volume(), R1.val().Volume())
