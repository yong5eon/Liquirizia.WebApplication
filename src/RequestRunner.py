# -*- coding: utf-8 -*-

from .Request import Request

from abc import ABC, abstractmethod

__all__ = (
	'RequestRunner',
)


class RequestRunner(object):
	"""Request Runner Interface"""

	@abstractmethod
	def __init__(self, request: Request, parameters):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

	@abstractmethod
	def run(self, body=None):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
