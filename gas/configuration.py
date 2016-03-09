import os
import imp

filename = os.path.join(os.getcwd(), 'settings.py')

if os.path.exists(filename):
	config = imp.load_source('settings', filename)
else:
	config = object()
