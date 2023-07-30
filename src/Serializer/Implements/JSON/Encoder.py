# -*- coding: utf-8 -*-

from collections.abc import Sequence, Mapping, Set
from datetime import datetime, date
from decimal import Decimal
from json import dumps, JSONEncoder

from ...Serializer import Serializer

__all__ = (
	'Encoder'
)


class TypeEncoder(JSONEncoder):
	"""
	Type Encoder for JSON
	"""

	def default(self, obj):
		if isinstance(obj, Decimal):
			return float(obj)
		if isinstance(obj, Sequence):
			return list(obj)
		if isinstance(obj, Mapping):
			return dict(obj)
		if isinstance(obj, Set):
			return tuple(obj)
		if isinstance(obj, (date, datetime)):
			return obj.isoformat()
		# TODO : support DataModelObject
		return None


class Encoder(Serializer):
	"""
	Encoder Class for JSON
	"""

	def __call__(self, obj):
		return dumps(obj, ensure_ascii=False, cls=TypeEncoder)
	
	
