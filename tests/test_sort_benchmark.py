from itertools import product
import pytest
from tnt.algorithms.sorting import (
	quick_sort,
	c_quick_sort,
	merge_sort,
	heap_sort
	)
from test_sorting import generate_array

__author__ = "trong-nguyen"
__copyright__ = "trong-nguyen"
__license__ = "GPL"

testing_pool = list(product(
	[10000],
	['unique', 'sorted', 'identical']
))

@pytest.fixture(
	scope='module',
	params=[generate_array(size, kind) for size, kind in testing_pool],
	ids=['n={} array={}'.format(size, kind) for size, kind in testing_pool]
	)
def get_validators(request):
	return request.param

class TestBenchmarkSort:
	def benchmark_api(self, sort_algorithm, benchmark, get_validators):
		array, _ = get_validators
		benchmark(sort_algorithm, array)

	@pytest.mark.benchmark(group='quick')
	def test_quick_sort(self, benchmark, get_validators):
		self.benchmark_api(quick_sort, benchmark, get_validators)

	@pytest.mark.benchmark(group='quick')
	def test_c_quick_sort(self, benchmark, get_validators):
		self.benchmark_api(c_quick_sort, benchmark, get_validators)
		
	def test_merge_sort(self, benchmark, get_validators):
		self.benchmark_api(merge_sort, benchmark, get_validators)
		
	@pytest.mark.benchmark(group='quick')
	def test_heap_sort(self, benchmark, get_validators):
		self.benchmark_api(heap_sort, benchmark, get_validators)

	@pytest.mark.benchmark(group='quick')
	def test_builtin(self, benchmark, get_validators):
		self.benchmark_api(sorted, benchmark, get_validators)