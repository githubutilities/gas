
def install_and_import(package):
	# http://stackoverflow.com/questions/12332975/installing-python-module-within-code
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
