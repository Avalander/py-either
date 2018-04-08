import unittest

from either import Either, Left, Right


class TestMaybe(unittest.TestCase):
	def test_maybe_should_return_left_when_value_is_none(self):
		actual = Either.maybe(None)
		self.assertIsInstance(actual, Left)

	def test_maybe_should_return_right_when_value_exists(self):
		actual = Either.maybe(3)
		self.assertIsInstance(actual, Right)

	def test_maybe_should_put_value_in_right(self):
		actual = Either.maybe('ponies').fold(
			self.fail,
			lambda x: x
		)
		self.assertEqual(actual, 'ponies')

class TestTryExcept(unittest.TestCase):
	def test_try_except_should_return_value_when_computation_does_not_throw(self):
		actual = Either.try_except(lambda: 3).fold(
			self.fail,
			lambda x: x
		)
		self.assertEqual(actual, 3)

	def test_try_except_should_return_right_when_computation_does_not_throw(self):
		actual = Either.try_except(lambda: 3)
		self.assertIsInstance(actual, Right)

	def test_try_except_should_pass_params_to_computation(self):
		actual = Either.try_except(lambda x: x, 'potato').fold(
			self.fail,
			lambda x: x
		)
		self.assertEqual(actual, 'potato')

class TestCond(unittest.TestCase):
	def test_cond_should_return_right_when_value_fulfills_predicate(self):
		actual = Either.cond(lambda x: x > 3, 4)
		self.assertIsInstance(actual, Right)

	def test_cond_should_return_right_with_value_when_it_fulfills_predicate(self):
		actual = Either.cond(lambda x: len(x) > 3, 'Twilight Sparkle').fold(
			self.fail,
			lambda x: x
		)
		self.assertEqual(actual, 'Twilight Sparkle')

	def test_cond_should_return_left_when_value_does_not_fulfill_predicate(self):
		actual = Either.cond(lambda x: x > 3, 2)
		self.assertIsInstance(actual, Left)

	def test_cond_should_return_left_without_value_when_it_does_not_fulfill_predicate(self):
		actual = Either.cond(lambda x: len(x) > 3, 'Mu').fold(
			lambda x: x,
			self.fail
		)
		self.assertIsNone(actual)

	def test_cond_should_return_left_with_error_value_when_provided(self):
		actual = Either.cond(lambda x: x > 0, -3, 'Value must be positive.').fold(
			lambda x: x,
			self.fail
		)
		self.assertEqual(actual, 'Value must be positive.')
