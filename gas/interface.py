def run(*args, **kwargs):
	_run(*args, **kwargs)

def _run(task=None):
	if task is None:
		return
	task()
