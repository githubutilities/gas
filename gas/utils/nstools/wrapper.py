# Assuming line is utf-8 format
from langconv import *
def convert(line, option='simplify'):
	# avoid decoding unicode because unicode has already been decoded
	if not isinstance(line, unicode):
		line = line.decode('utf-8')

	if option is 'simplify':
		converter = Converter('zh-hans')
	elif option is 'traditional':
		converter = Converter('zh-hant')

	line = converter.convert(line)
	return line
