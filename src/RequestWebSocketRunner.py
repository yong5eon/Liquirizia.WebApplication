# -*- coding: utf-8 -*-

from .RequestRunner import RequestRunner
from .WebSocket import WebSocket

from abc import abstractmethod

__all__ = (
	'RequestWebSocketRunner',
)


class RequestWebSocketRunner(RequestRunner):
	"""Request Runner Interface for Web Socket"""

	@abstractmethod
	def run(self, ws: WebSocket, op, buffer):
		raise NotImplementedError('{} must be implemented run'.format(self.__class__.__name__))
