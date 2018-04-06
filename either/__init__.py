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

	@classmethod
	def maybe(cls, value):
		if value is not None:
			return Right(value)
		return Left()

	@classmethod
	def try_except(cls, computation, *args):
		try:
			result = computation(*args)
			return Right(result)
		except Exception as e:
			return Left(e)

	@classmethod
	def cond(cls, predicate, *args):
		if (predicate(*args)):
			return Right(None)
		return Left()

Either.register(Left)
Either.register(Right)
