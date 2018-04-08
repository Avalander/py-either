import unittest

from either import Left, Right


class TestMap(unittest.TestCase):
	def test_right_should_return_right(self):
		actual = Right(3)
		self.assertIsInstance(actual, Right)

	def test_map_should_return_right(self):
		actual = Right(3).map(lambda x: x + 1)
		self.assertIsInstance(actual, Right)

	def test_map_should_apply_transformation_to_value(self):
		actual = Right(3).map(lambda x: x + 1).fold(
			self.fail,
			lambda x: x
		)
		self.assertEqual(actual, 4)

class TestChain(unittest.TestCase):
	def test_chain_should_fail_if_fn_does_not_return_either(self):
		either = Right(3)
		self.assertRaises(TypeError, either.chain, lambda x: x)

	def test_chain_should_return_the_right_returned_by_computation(self):
		expected = Right(4)
		actual = Right(3).chain(lambda x: expected)

		self.assertIs(actual, expected)
	
	def test_chain_should_return_the_left_returned_by_computation(self):
		expected = Left()
		actual = Right(3).chain(lambda x: expected)

		self.assertIs(actual, expected)

class TestFold(unittest.TestCase):
	def test_fold_should_run_right_branch(self):
		actual = Right(3).fold(
			self.fail,
			lambda x: x
		)
		self.assertEqual(actual, 3)
