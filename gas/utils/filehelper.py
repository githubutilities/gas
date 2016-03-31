import os
import codecs
from gas import config as settings

class DataPathException(Exception):
	pass

class open_data(object):
	"""
	open data

	# API Design Reference, https://docs.python.org/2/library/codecs.html
	open_data(filename, mode[, encoding])
	"""
	def __init__(self, filename, mode, encoding="utf-8", path=None):
		super(open_data, self).__init__()
		self._filename = filename
		self._mode = mode
		self._encoding = encoding
		self._data_path = path

	@property
	def _datadir(self):
		if self._data_path is None:
			if not hasattr(settings, 'DATA_PATH'):
				raise DataPathException('Data path not set')
			else:
				self._data_path = settings.DATA_PATH

		if not os.path.exists(self._data_path):
			os.makedirs(self._data_path)

		return self._data_path

	@property
	def _file(self):
		# Get class name by `self.__class__.__name__`
		if not hasattr(self, '_open_data__file'):
			filepath = os.path.join(self._datadir, self._filename)
			self.__file = codecs.open(filepath, self._mode, self._encoding)
		return self.__file
	
	# Python With Statement, http://effbot.org/zone/python-with-statement.htm
	def __enter__(self):
		return self._file

	def __exit__(self, type, value, traceback):
		self._file.close()


def open_dataframe(name, **kwargs):
	import pandas as pd
	with open_data(name, 'r') as f:
		df = pd.read_csv(f, **kwargs)
	return df
