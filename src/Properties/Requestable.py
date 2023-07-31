# -*- coding: utf-8 -*-

from ..Request import Request

from abc import ABC, abstractmethod

__all__ = (
	'Requestable'
)


class Requestable(ABC):
	"""Requestable Interface"""
	@abstractmethod
	def request(self) -> Request:
		raise NotImplementedError('{} must be implemented request'.format(self.__class__.__name__))
