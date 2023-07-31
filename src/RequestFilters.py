# -*- coding: utf-8 -*-

from .Request import Request
from .Response import Response
from .ResponseFilter import ResponseFilter

__all__ = (
	'RequestFilters',
)


class RequestFilters(ResponseFilter):
	"""Request Fileters"""
	def __init__(self, *args):
		self.filters = args
		return

	def run(self, request: Request) -> Request:
		for f in self.filters:
			request, response = f.run(request)
			if response:
				return request, response
		return request, None
