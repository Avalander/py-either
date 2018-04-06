from abc import ABC


class Left:
	def __init__(self, value=None):
		self._value = value

	def __repr__(self):
		return 'Either.Left({})'.format(self._value if self._value is not None else '')

	def map(self, fn):
		return self

	def chain(self, fn):
		return self

	def fold(self, fn_l, fn_r):
		return fn_l(self._value)


class Right:
	def __init__(self, value):
		self._value = value

	def __repr__(self):
		return 'Either.Right({})'.format(self._value)

	def map(self, fn):
		return Right(fn(self._value))

	def chain(self, fn):
		result = fn(self._value)
		if not isinstance(result, Either):
			reason = 'Either.chain(a -> Either(a)) expected callback that returns an Either, but returned {} instead'.format(type(result))
			raise TypeError(reason)
		return result

	def fold(self, fn_l, fn_r):
		return fn_r(self._value)


class Either(ABC):
	@classmethod
	def Left(cls, value=None):
		return Left(value)

	@classmethod
	def Right(cls, value):
		return Right(value)

Either.register(Left)
Either.register(Right)


if __name__ == '__main__':
	result = (Either.Right(153)
		.map(lambda x: x + 1)
		.chain(lambda x: Left(x) if x < 150 else Right(x))
		.fold(
			lambda x: 'left {}'.format(x),
			lambda y: 'right {}'.format(y)))
	print(result)
	print(Left('potato'))
