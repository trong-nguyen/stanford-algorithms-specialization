###
# Great to see you, my name is Trong.
###


# moves = [ 3, 2, 1, 9, 0, 2, 4, 5, -4, 15]
# capacity = 10
# power = capacity - moves[0]
# lower_capacity = power
# for m1, m0 in zip(moves[1:], moves[0:-1]):
#     dm = -m1+m0
#     power += min(dm, capacity)
#     lower_capacity = min(lower_capacity, power)
#     print power
    
# print 'Suggested capacity {}'.format(capacity-lower_capacity)


import random

def add_integers(s1,s2,band=3):
    def partitions (s, n):
        return [ s[n*i:min(len(s), n*(i+1))] for i in range(len(s)/n+1) ] 
                
    p1 = partitions(s1,band)
    
    p2 = partitions(s2,band)
    
    
# add_integers('1232342349', '12',3)

class Queue:
    def __init__(self, n=3):
        self.data = [False]*n
        self.tail = 0
        self.head = 0
        self.count = 0
    def enqueue(self, item):
        if self.count == len(self.data):
            if self.head >= self.tail:
                self.data =  self.data[self.head:] + self.data[:self.tail] + [False] * len(self.data)
            else:
                self.data += [False] * len(self.data)
            self.head = 0
            self.tail = len(self.data)/2
            
        self.data[self.tail] = item
        self.tail = (self.tail + 1) % len(self.data)
        self.count += 1
        self.show()
        
    def dequeue(self):
        if self.count:
            item = self.data[self.head]
            self.data[self.head] = False
            self.head = (self.head + 1) % len(self.data)
            self.count -= 1
            
            self.show()
            return item
        
    def show(self):
        print ' '.join( [ i if i else '_' for i in self.data ] )
        
        
def test_queue():
    q = Queue()
    for i in 'abc':
        q.enqueue(i)
    q.dequeue()
    for i in 'defgh':
        q.enqueue(i)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    for i in 'ijklmnopqr':
        q.enqueue(i)
        
    print 'Verified result:'
    print '''
f g h i j k l m n o p q r _ _ _ _ _ _ _ _ _ _ _
'''
        
        
# test_queue()



def quick_sort(a, start, end):
    # http://www.algolist.net/Algorithms/Sorting/Quicksort
    def select_pivot(s, e):
        return s

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
        quick_sort(a, start, pivot-1)
    if pivot < end:
        quick_sort(a, pivot, end)
    return a

def tnt_quick_sort(a):
    if not isinstance(a, list):
        raise 'tnt_quick_sort supports lists of ints only'

    import tnt
    return tnt.quick_sort(a)

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
    import operator
    heap = Heap(operator.gt)
    heap.sort(unsorted)
    return unsorted



def bubble_sort(unsorted):
    def do_1_pass(a):
        swapped = False
        for i,(u,v) in enumerate( zip(a[1:], a[:-1]) ):
            if u < v:
                a[i+1], a[i] = a[i], a[i+1]
                swapped = True
        return swapped
    while do_1_pass(unsorted):
        pass
    return unsorted

def insertion_sort(unsorted):
    def insert(a, i):
        while i > 0:
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]
                i -= 1
            else:
                break
    for i in xrange(1, len(unsorted)):
        insert(unsorted, i)
    return unsorted

# http://stackoverflow.com/questions/889900/accurate-timing-of-functions-in-python
import time
def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))

        print(endTime - startTime,'ms')
        return result

    return wrapper

def test_sort_mechanism(sorter, a, validate=None, display=True, vargs=[]):
    @timeme
    def time_algorithm(sorter, a, vargs):
        return sorter(a, *vargs)

    b = list(a)
    b = time_algorithm(sorter, b, vargs)
    print 'Testing', sorter
    if validate:
        print 'Sorting correctness is', b == validate
    if display:
        print b

    
from collections import defaultdict
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

def test_sort():
    N = 100000
    arrays = [ [ random.randint(0,N) for i in range(N) ] for j in range(3) ]
    array = [ ai for a in arrays for ai in a ]
    display = False
    validate = sorted(array)
    # test_sort_mechanism( merge_sort, array, validate, display )
    test_sort_mechanism( quick_sort, array, validate, display=display, vargs=[0, len(array)-1] ) #wrong
    test_sort_mechanism( tnt_quick_sort, array, validate, display=display)
    # test_sort_mechanism( heap_sort, array, validate, display )
    # test_sort_mechanism( bubble_sort, array, validate, display )
    # test_sort_mechanism( insertion_sort, array, validate, display )
    test_sort_mechanism( sorted, array, validate, display )

    sa = [ sorted(a) for a in arrays ]
    # test_sort_mechanism( k_heap_sort, sa, validate, display, vargs=[9] )

if __name__ == '__main__':
    test_sort()