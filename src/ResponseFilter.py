# -*- coding: utf-8 -*-

from .Response import Response

from abc import ABC, abstractmethod

__all__ = (
	'ResponseFilter',
)


class ResponseFilter(ABC):
	"""Request Filter Interface"""

	@abstractmethod
	def run(self, response: Response) -> Response:
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
