#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import random
from itertools import product
from tnt.algorithms.sorting import (
	merge_sort,
	quick_sort,
	c_quick_sort,
	heap_sort,
	bubble_sort,
	insertion_sort,
	k_heap_sort
	)


__author__ = "trong-nguyen"
__copyright__ = "trong-nguyen"
__license__ = "GPL"

def generate_array(n, kind, **kwargs):
	if kind == 'unique':
		a = [random.randint(0,n) for i in range(n)]
		return a, sorted(a)
	elif kind == 'duplicated':
		dup = kwargs.get('dup', 4) # default 4 if not provided
		a = [random.randint(0,n/dup) for i in range(n)]
		return a, sorted(a)
	elif kind == 'sorted':
		a = list(range(n))
		return a, a
	elif kind == 'identical':
		a = [random.randint(0,n)] * n
		return a, a
	else:
		raise 'Invalid array kind {}'.format(kind)

testing_pool = list(product(
	[1, 10, 1000],
	['unique', 'duplicated', 'sorted', 'identical']
))

@pytest.fixture(
	scope='module',
	params=[generate_array(size, kind) for size, kind in testing_pool],
	ids=['n={} array={}'.format(size, kind) for size, kind in testing_pool]
	)
def get_validators(request):
	return request.param


class TestSort:
	# the common testing skeleton for any sort algorithm
	def sort_test_api(self, sort_algorithm, get_validators):
		array, expected = get_validators
		result = sort_algorithm(array)
		assert result == expected

	def test_merge_sort(self, get_validators):
		self.sort_test_api(merge_sort, get_validators)

	def test_quick_sort(self, get_validators):
		self.sort_test_api(quick_sort, get_validators)

	def test_c_quick_sort(self, get_validators):
		self.sort_test_api(c_quick_sort, get_validators)
		
	def test_heap_sort(self, get_validators):
		self.sort_test_api(heap_sort, get_validators)
		
	def test_bubble_sort(self, get_validators):
		self.sort_test_api(bubble_sort, get_validators)
		
	def test_insertion_sort(self, get_validators):
		self.sort_test_api(insertion_sort, get_validators)
		
	def test_quick_sort(self, get_validators):
		self.sort_test_api(quick_sort, get_validators)