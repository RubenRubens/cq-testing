import unittest

class TestLoft(unittest.TestCase):

	# Import and validate
	def test_L(self):
		import loft.L
		global R1
		R1 = loft.L.result
		self.assertTrue(R1.val().isValid())

	# Import the geometry made in Fusion 360
	def test_importSTEP(self):
		from cadquery import importers
		global R2
		R2 = importers.importStep('loft/L.step')
		self.assertTrue(R2.val().isValid())

	# Compare the volumes directly
	def test_volume_directly(self):
		self.assertAlmostEqual(R1.val().Volume() / R2.val().Volume(), 1, delta=0.01)

	# Compare the volumes using boolean operations
	def test_volume_boolean(self):
		from cadquery import importers
		R2 = importers.importStep('loft/L.step')
		self.assertAlmostEqual(R1.cut(R2).val().Volume(), 0, delta=400)
		self.assertAlmostEqual(R1.union(R2).val().Volume(), R1.val().Volume(), delta=400)
		self.assertAlmostEqual(R1.intersect(R2).val().Volume(), R1.val().Volume(), delta=400)
