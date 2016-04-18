import os
import pickle

from .module_helper import caller_name


DEFAULT_PATH = os.path.join(os.path.abspath(os.getcwd()))


class PickleHelper(object):
	def __init__(self, path=None):
		if path is None:
			self._init_cache_path(path)
		else:
			self._init_cache_path()

	def _init_cache_path(self, path=DEFAULT_PATH):
		cache_path = os.path.join(path, '.gas')
		if not os.path.exists(cache_path):
			os.makedirs(cache_path)
		self.cache_path = cache_path

	def _dump_cache(self, filepath, obj):
		with open(filepath, 'w') as f:
			pickle.dump(obj, f)

	def _load_cache(self, filepath):
		with open(filepath, 'r') as f:
			ret = pickle.load(f)
		return ret

	def _get_filepath(self, obj_name):
		filename = "{}.{}".format(caller_name(skip=4), obj_name)
		filepath = os.path.join(self.cache_path, filename)
		return filepath

	def load(self, obj_name):
		filepath = self._get_filepath(obj_name)
		print filepath
		if os.path.exists(filepath):
			return self._load_cache(filepath)
		else:
			return None

	def save(self, obj_name, obj):
		filepath = self._get_filepath(obj_name)
		print filepath
		self._dump_cache(filepath, obj)


def save(obj_name, obj, path=DEFAULT_PATH):
	cache = PickleHelper(path=path)
	cache.save(obj_name, obj)


def load(obj_name, path=DEFAULT_PATH):
	cache = PickleHelper(path=path)
	return cache.load(obj_name)
