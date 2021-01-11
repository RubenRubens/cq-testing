import unittest

class TestThread(unittest.TestCase):

	# Import and validate T1
	def test_T1(self):
		import src.Thread.T1
		R1 = src.Thread.T1.result
		self.assertTrue(R1.val().isValid())

	# Import and validate T2
	def test_T2(self):
		import src.Thread.T2
		R2 = src.Thread.T2.result
		self.assertTrue(R2.val().isValid())

	# Tests if the objects are equal
	def test_equal(self):
		self.assertEqual(R1.cut(R2).val().Volume(), 0)
		self.assertEqual(R1.union(R2).val().Volume(), R1.val().Volume())
		self.assertEqual(R1.intersect(R2).val().Volume(), R1.val().Volume())
