import six

from .module_helper import import_non_local

time = import_non_local('time')

import inspect

def caller_name(skip=2):
	"""Get a name of a caller in the format module.class.method
	
	   `skip` specifies how many levels of stack to skip while getting caller
	   name. skip=1 means "who calls me", skip=2 "who calls my caller" etc.
	   
	   An empty string is returned if skipped levels exceed stack height
	"""
	stack = inspect.stack()
	start = 0 + skip
	if len(stack) < start + 1:
		return ''
	parentframe = stack[start][0]    
	
	name = []
	module = inspect.getmodule(parentframe)
	# `modname` can be None when frame is executed directly in console
	# TODO(techtonik): consider using __main__

	if module:
		name.append(module.__name__)
	# detect classname
	if 'self' in parentframe.f_locals:
		# I don't know any way to detect call from the object method
		# XXX: there seems to be no way to detect static method call - it will
		#      be just a function call
		name.append(parentframe.f_locals['self'].__class__.__name__)
	codename = parentframe.f_code.co_name
	if codename != '<module>':  # top level usually
		name.append( codename ) # function or a method
	del parentframe
	return ".".join(name)

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
		