import unittest

from either import Left, Right


class TestLeft(unittest.TestCase):
	def test_left_should_return_left_instance_when_called_with_no_value(self):
		actual = Left()
		self.assertIsInstance(actual, Left)

	def test_left_should_return_left_instance_when_called_with_value(self):
		actual = Left(3)
		self.assertIsInstance(actual, Left)

class TestMap(unittest.TestCase):
	def test_map_should_not_apply_transformation(self):
		actual = Left(3).map(lambda x: x + 1).fold(
			lambda x: x,
			lambda x: x
		)
		self.assertEqual(actual, 3)

	def test_map_should_return_left_instance(self):
		actual = Left(3).map(lambda x: x + 1)
		self.assertIsInstance(actual, Left)

class TestChain(unittest.TestCase):
	def test_chain_should_return_left_instance(self):
		actual = Left().chain(lambda x: Right(4))
		self.assertIsInstance(actual, Left)

	def test_chain_should_not_apply_transformation(self):
		actual = Left().chain(lambda x: Right(4)).fold(
			lambda x: x,
			self.fail
		)
		self.assertIsNone(actual)

class TestFold(unittest.TestCase):
	def test_fold_should_run_left_branch(self):
		actual = Left(3).fold(
			lambda x: x + 1,
			self.fail
		)
		self.assertEqual(actual, 4)
