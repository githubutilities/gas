import six

from .module_helper import import_non_local
from .module_helper import caller_name

time = import_non_local('time')


def hms_string(sec_elapsed):
	"""Please refer to https://arcpy.wordpress.com/2012/04/20/146/"""
	h = int(sec_elapsed / (60 * 60))
	m = int((sec_elapsed % (60 * 60)) / 60)
	s = sec_elapsed % 60.
	return "{}:{:>02}:{:>05.2f}".format(h, m, s)

def timeit(f):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = f(*args, **kwargs)
		elapsed = time.time() - start

		log_msg = "{} took {} time to finish".format(caller_name(), hms_string(elapsed))
		six.print_(log_msg)
	return wrapper
		