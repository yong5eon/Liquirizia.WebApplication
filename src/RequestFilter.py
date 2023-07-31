# -*- coding: utf-8 -*-

from .Request import Request
from .Response import Response

from abc import ABC, abstractmethod

__all__ = (
	'RequestFilter',
)


class RequestFilter(ABC):
	"""Request Filter Interface"""
	@abstractmethod
	def run(self, request: Request) -> Request:
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
