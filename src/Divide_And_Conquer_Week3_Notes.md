> Let 0<α<.5 be some constant (independent of the input array length n). Recall the Partition subroutine employed by the QuickSort algorithm, as explained in lecture. What is the probability that, with a randomly chosen pivot element, the Partition subroutine produces a split in which the size of the smaller of the two subarrays is ≥α times the size of the original array?

The problem should be rephrased as: given a number 0<α<.5, what is the probability that the smaller of the partitioned sub-arrays has size equal or larger than α times the original array, assumed uniform distribution of choosen pivot element.

And then it would be easier to imagine the solution: what are the chances that we would have sub array sizes e.or.l than α. Given 0<α<.5, there are 2 * (0.5 - α) chances of cutting the original array that the smaller array has size >= α. 

Imagine this illustration: o--x----|----x--o.  
Segment o--x = α.  
Segment x----|----x (note: symmetric) is the space representing the chance that we end up having array size larger than α. It would be (due to symmetry): (0.5 - α) * 2.