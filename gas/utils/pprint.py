# -*- coding: utf-8 -*-

__all__ = ["_my_safe_repr"]

from .module_helper import import_non_local

_pprint = import_non_local('pprint', 'std_pprint')

# Fix `repr()` problem with chinese character
def _my_safe_repr(object, context, maxlevels, level):
	repr, readable, recursive = _pprint._safe_repr(object, context, maxlevels, level)
	# * pprint chinese bug is at [here]
	#	https://github.com/python/cpython/blob/master/Lib/pprint.py#L555
	# * [repr function problem in python 2]
	#	http://stackoverflow.com/questions/2261593/python-repr-function-problem
	# * [repr between python 2 and python 3]
	# 	http://stackoverflow.com/questions/13329273/word-counter-wont-print-foreign-characters
	# Use eval to undo `repr()`
	typ = _pprint._type(object)
	if typ is unicode:
		my_repr = eval(repr)
	else:
		my_repr = repr
	return my_repr, readable, recursive

def pprint(object, stream=None, indent=1, width=80, depth=None, compact=False):
	"""Pretty-print a Python object to a stream [default is sys.stdout]."""

	printer = _pprint.PrettyPrinter( \
		stream=stream, indent=indent, width=width, depth=depth)#, compact=compact)
	printer.format = _my_safe_repr
	printer.pprint(object)

# class _PPrint(object):
# 	"""_PPrint"""
# 	def __init__(self):
# 		super(_PPrint, self).__init__()

# 	@property
# 	def pprint(self):
# 		print dir(_pprint)
# 		printer = _pprint.PrettyPrinter()
# 		printer.format = _my_safe_repr
# 		# printer.pprint(object)
# 		return _pprint.pprint
# import sys
# sys.modules[__name__] = _PPrint()

# Reference
#*[module property](http://stackoverflow.com/questions/880530/can-python-modules-have-properties-the-same-way-that-objects-can)
