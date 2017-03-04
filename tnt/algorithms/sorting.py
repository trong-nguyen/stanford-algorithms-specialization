from tnt.algorithms import ext
import operator
from collections import defaultdict

'''
sort API:
sort(array):
    non-mutated
    return new array
'''

def swap_array_elms(a, i, j):
    a[i], a[j] = a[j], a[i]

def merge_sort(unsorted):
    def merge(a,b):
        ac, bc = a, b
        s = []
        while ac or bc:
            if not ac:
                s += bc
                bc = []
            elif not bc:
                s += ac
                ac = []
            elif bc[0] < ac[0]:
                s += [ bc[0] ]
                bc = bc[1:]
            else:
                s += [ ac[0] ]
                ac = ac[1:]
        return s
        
    n = len(unsorted)
    if n == 1:
        return unsorted
    a,b = merge_sort( unsorted[:n/2] ), merge_sort( unsorted[n/2:] )
    return merge(a,b)

def quick_sort(a):
    def _quick_sort(a, start, end):
        # http://www.algolist.net/Algorithms/Sorting/Quicksort
        def select_pivot(s, e):
            return (s+e)/2

        def partition(a, s, e):
            ap = a[select_pivot(s, e)]
            i, j = s, e
            while i <= j:
                while a[i] < ap:
                    i += 1

                while a[j] > ap:
                    j -= 1
                    
                # print i, j, a[s:e]

                if i <= j:
                    swap_array_elms(a, i, j)
                    i += 1
                    j -= 1
                # print j, select_pivot(s, e), ap, a[s:e]
            return i

        if start >= end:
            return a 
        pivot = partition(a, start, end)
        if start < pivot-1:
            _quick_sort(a, start, pivot-1)
        if pivot < end:
            _quick_sort(a, pivot, end)
        return a

    b = list(a)
    return _quick_sort(b, 0, len(b)-1)


def c_quick_sort(a):
    # The same algorithm as quick_sort but implemented in C++
    if not isinstance(a, list):
        raise 'tnt_quick_sort supports lists of ints only'

    return ext.quick_sort(a)

class Heap:
    def __init__(self, compare):
        self.compare = compare # comparison operator

    # http://www.cs.toronto.edu/~krueger/cscB63h/w07/lectures/tut02.txt
    @staticmethod
    def heapify(a, i, n, compare):
        l = 2*i+1
        r = 2*i+2
        if l < n and r < n:
            c = r if compare( a[r], a[l] ) else l
        elif l < n:
            c = l
        elif r < n:
            c = r
        else:
            return
        
        if compare(a[c], a[i]):
            a[i], a[c] = a[c], a[i]
            Heap.heapify(a, c, n, compare) # correct destroyed properties due to swap

    def build(self, a):
        for i in xrange(len(a)/2-1,-1,-1):
            self.heapify(a,i,len(a), self.compare)

    def sort(self, a):
        self.build(a)
        for i in xrange(len(a)-1,0,-1):
            a[i], a[0] = a[0], a[i]
            self.heapify(a, 0, i, self.compare)

    def pop(self, a):
        if not a:
            return None
        n = len(a)
        am, a[0] = a[0], a[n-1]
        self.heapify(a, 0, n-1, self.compare)
        del a[n-1]
        return am

def heap_sort(unsorted):
    heap = Heap(operator.gt)
    b = list(unsorted)
    heap.sort(b)
    return b

def bubble_sort(unsorted):
    def do_1_pass(a):
        swapped = False
        for i,(u,v) in enumerate( zip(a[1:], a[:-1]) ):
            if u < v:
                a[i+1], a[i] = a[i], a[i+1]
                swapped = True
        return swapped

    b = list(unsorted)
    while do_1_pass(b):
        pass
    return b

def insertion_sort(unsorted):
    def insert(a, i):
        while i > 0:
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]
                i -= 1
            else:
                break
    b = list(unsorted)
    for i in xrange(1, len(b)):
        insert(b, i)
    return b



def k_heap_sort(arrays, k):
    for i, a in enumerate(arrays):
        arrays[i] = sorted(a)
    m = len(arrays)
    c = k/m # length of small extractions'
    def pick_first_k_items(a, k):
        return a[:k], a[k:]
    heap_array = []

    for idx, a in enumerate(arrays):
        ak, ka = pick_first_k_items(a, c)
        heap_array += [ (idx, v) for v in ak ]
        arrays[idx] = ka

    heap = Heap( compare=lambda u, v: u[1] < v[1] )
    heap.build(heap_array)
    sorted_array = []
    
    while heap_array:
        popped_idx = defaultdict(lambda: 0)
        for i in xrange(c):
            r = heap.pop(heap_array)
            if r:
                idx, v = r
                sorted_array.append(v)
                # print 'sorted', sorted_array
                popped_idx[idx] += 1

        for idx,v in popped_idx.items():
            r = pick_first_k_items(arrays[idx], v)
            if r:
                ak, ka = r
                heap_array = [ (idx, aki) for aki in ak ] + heap_array
                arrays[idx] = ka

        # heap_array = sorted(heap_array)
        heap.build(heap_array)

    return sorted_array