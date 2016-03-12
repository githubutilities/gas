import os
import sys
import time
import imp
import runpy
import traceback
import argparse
import logging
from multiprocessing import Process

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def run_module(module, function=None):
	if function is not None: # run it as a module
		module = os.sep.join(module.split('.'))
		pwd = os.path.dirname(os.path.abspath(__file__))

		module_path = os.path.join(pwd, module)
		if os.path.isdir(module_path):
			module_path = os.path.join(module_path, '__init__.py')
		else:
			module_path = "{}.py".format(module_path)

		module = imp.load_source('module', module_path)

		if hasattr(module, function):
			getattr(module, function)()
	else:
		try:
			runpy.run_module(module, run_name="__main__", alter_sys=True)
			# Reference
			# https://docs.python.org/2/library/runpy.html
		except Exception, e:
			exec_info = sys.exc_info()
			traceback.print_exception(*exec_info)

class ChangeAndRunEventHandler(PatternMatchingEventHandler):
	"""docstring for ChangeAndRunEventHandler"""
	def __init__(self, module, function=None, patterns=None, ignore_patterns=None, 
			ignore_directories=False, case_sensitive=False):
		super(ChangeAndRunEventHandler, self).__init__(patterns, ignore_patterns,
				ignore_directories, case_sensitive)
		self.module = module
		self.function = function
		self.proc = None

	def on_any_event(self, event):
		pass

	def on_moved(self, event):
		pass

	def on_created(self, event):
		pass

	def on_deleted(self, event):
		pass

	def on_modified(self, event):
		# if previous process is still alive, kill it
		if hasattr(self.proc, 'is_alive') and self.proc.is_alive():
			sys.stdout.write('terminating')
			while self.proc.is_alive():
				sys.stdout.write('.')
				self.proc.terminate()
				time.sleep(0.5)
			sys.stdout.write('\n\n\n')
		os.system('clear')
		# create new process after ensuring that the process has been killed
		self.proc = Process(target=run_module, args=(self.module, self.function, ))
		self.proc.start()
		# https://docs.python.org/3/library/multiprocessing.html

def monitor_module(module, function=None):
	logging.basicConfig(level=logging.INFO,
						format='%(asctime)s - %(message)s',
						datefmt='%Y-%m-%d %H:%M:%S')

	path = '.'#os.sep.join(path.split('.'))
	pwd = os.path.dirname(os.path.abspath(__file__))

	module_path = os.path.join(pwd, path)
	event_handler = ChangeAndRunEventHandler(module, function=function, patterns=['*.py'])
	observer = Observer()
	observer.schedule(event_handler, path, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(1)
			# observer.join()
	except KeyboardInterrupt:
		observer.stop()
	observer.join()

def gasd(argv=sys.argv[1:]):
	parser = argparse.ArgumentParser(prog='gas', usage='%(prog)s <module>', 
		description=u'Central %(prog)s station debugger')
	parser.add_argument(u'--module', nargs='?', help=u'Debug in module mode')

	opts = parser.parse_args(argv)

	if opts.module:
		monitor_module(opts.module)
	else:
		parser.print_help()

def gas_run(argv=sys.argv[1:]):
	gasd()
