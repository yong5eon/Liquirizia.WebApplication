# -*- coding: utf-8 -*-

from .RequestRunner import RequestRunner
from .RequestReader import RequestReader
from .ResponseWriter import ResponseWriter

from abc import abstractmethod

__all__ = (
	'RequestStreamRunner',
)


class RequestStreamRunner(RequestRunner):
	"""Request Runner Interface for Stream"""

	@abstractmethod
	def run(self, reader: RequestReader, writer: ResponseWriter):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
