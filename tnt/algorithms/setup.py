from distutils.core import setup, Extension

module = Extension('tnt', 
	sources=['quick_sort.cpp'])

setup(name='TNT',
	version='1.0',
	description='Quick sort algorithm',
	# packages=['tnt'],
	ext_modules=[module])
