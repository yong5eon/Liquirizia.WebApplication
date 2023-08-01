# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

__all__ = (
	'Object'
)


class Object(ABC):
	"""Multi Part Form Data Object Interface"""

	@abstractmethod
	def headers(self):
		raise NotImplementedError('{} must be implemented headers'.format(self.__class__.__name__))

	@abstractmethod
	def body(self):
		raise NotImplementedError('{} must be implemented body'.format(self.__class__.__name__))
