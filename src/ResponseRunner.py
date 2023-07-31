# -*- coding: utf-8 -*-

from .Response import Response

from abc import ABC, abstractmethod

__all__ = (
	'ResponseRunner',
)


class ResponseRunner(ABC):
	"""Response Runner Interface"""

	@abstractmethod
	def run(self, request: Response, body: any = None):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
