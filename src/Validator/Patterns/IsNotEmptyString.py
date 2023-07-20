# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Error import Error
from ..ErrorResponse import ErrorResponse

from ...Response import Response

__all__ = (
	'IsNotEmptyString'
)


class IsNotEmptyString(Pattern):
	def __init__(self, error: Error = None, errorResponse: ErrorResponse = None):
		self.error = error
		self.errorResponse = errorResponse
		return

	def __call__(self, parameter) -> (any, (Response, None)):
		try:
			if not isinstance(parameter, str):
				if self.error:
					raise self.error(parameter)
				raise RuntimeError('{} is not string'.format(parameter))
			if len(str(parameter)) == 0:
				if self.error:
					raise self.error(parameter)
				raise RuntimeError('{} is empty'.format(parameter))
			return parameter, None
		except BaseException as e:
			if self.errorResponse:
				return parameter, self.errorResponse(parameter)
			raise e