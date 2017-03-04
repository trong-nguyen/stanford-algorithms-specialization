#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for algorithms.

    This file was generated with PyScaffold 2.5.7, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import sys
from setuptools import setup, Extension, find_packages
# c_ext = Extension("facs/_facs", define_macros = [('DEBUG', '1'), ('FIFO', '1'), ('FILE_OFFSET_BITS', '64'), ('LARGE_FILE', '1')],
#                            sources = ["facs/facs.c", "facs/tool.c", "facs/bloom.c", "facs/good_build.c",
#                                       "facs/suggestions.c", "facs/lookup8.c", "facs/file_dir.c",
#                                       "facs/simple_check_1_ge.c", "facs/big_query.c", "facs/simple_remove.c"],
#                              extra_compile_args = ['-fopenmp'],
#                              extra_link_args=['-lgomp', '-lz'])
module = Extension('tnt.algorithms.ext', 
	sources=['tnt/algorithms/extensions/quick_sort.cpp'])


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['six', 'pyscaffold>=2.5a0,<2.6a0'] + sphinx,
          use_pyscaffold=True,
          version='0.1',
          packages=find_packages(),
          ext_modules=[module]
          )


if __name__ == "__main__":
    setup_package()
