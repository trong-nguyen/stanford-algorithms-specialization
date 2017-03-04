#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import random
from tnt.algorithms.skeleton import fib
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
__license__ = "GNU"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)

class TestSort:
	def generate_random(self):
		n = 1000
		random_array = [ random.randint(0,n) for i in range(n) ]
		sorted_random_array = sorted(random_array)
		return random_array, sorted_random_array

	def test_quick_sort(self, benchmark):
		arg, expected = self.generate_random()
		result = quick_sort(arg)
		assert result == expected


def load_sorters(array, expected):
	for sorter in (
		merge_sort,
		quick_sort,
		c_quick_sort,
		heap_sort,
		bubble_sort,
		insertion_sort,
	):
		assert sorter(array) == expected

	k = 4
	arrays = [array] * k
	expected_arrays = sorted([i for a in arrays for i in a])
	assert k_heap_sort(arrays, k) == expected_arrays

def test_sort_random_unique(benchmark):
	n = 1000
	array = [ random.randint(0,n) for i in range(n) ]
	expected = sorted(array)
	benchmark(load_sorters, array, expected)

def test_sort_random_duplicate():
	n = 1000
	num_duplicates = 4
	array = [ random.randint(0,n/num_duplicates) for i in range(n) ]
	expected = sorted(array)
	load_sorters(array, expected)

def test_sort_sorted():
	n = 1000
	array = list(range(n))
	load_sorters(array, array)

def test_sort_identical():
	n = 1000
	array = [random.randint(0,n)] * n
	load_sorters(array, array)