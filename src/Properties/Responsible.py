# -*- coding: utf-8 -*-

from ..Response import Response

from abc import ABC, abstractmethod

__all__ = (
	'Responsible'
)


class Responsible(ABC):
	"""Responseable Interface"""
	@abstractmethod
	def response(self) -> Response:
		raise NotImplementedError('{} must be implemented response'.format(self.__class__.__name__))
