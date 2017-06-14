# Algorithms Specialization - Coursera
School: Coursera  
Class: Algorithms Divide and Conquer  
Lecturer: Tim Roughgarden - Professor at Stanford University  
Published: 2012  

# Algorithm Design Analysis
Algorithms use one or more of the following methods:
- Divide and conquer  
Sorting algorithms (merge, quick)
- Randomized algorithms  
Quick sort
- Dynamic programming  
Fractional knapsack problem
- Greedy method: relies on the local **optimal subtructure** property of the problem.  
Dijkstras's method, activity selection, 0-1 (binary) Knapsack problem

### Dynamic programming vs Greedy method:
Algorithms that use greedy method differ from those using dynamic programming in the following ways:
- In dynamic programming, the solution to a problem depends on the solution to its subproblem. While in greedy method, the solution only depends on the information local to that paticular subproblem. This results in the following consequence.
- Dynamic programming uses bottom-up approach, greedy method uses top-down.

## Minimum Spanning Tree (MST) - Prim's Algorithm
Complexity: O(mlogn) using heap

Foundation on:
- Prim's algorithm guarantees to output a spanning tree (not neccessarily minimum): this in turn relies on:
	+ Empty cut property (zero cut <-> disconnected): guarantees the algorithm continues untill all vertices are included.
	+ Double-crossing cut property: assure no cycle produced since Prim's algorithm advances 1 edge at the time, and that edge has no loop back (thanks to the removal step after inclusion).
- **Cut Property**: if there exists a cut (A, B) of graph G and e is the cheapst crossing edge between A and B **THEN** e belongs to a MST (the MST if all costs are distinct) of G. 

Algorithm: proceeding similar to Dijkstra's algorithm. From one of the node in the frontier (minimum-degree vertices), continuously adding vertices (with the least cost connected edge) to the spanning tree and keeping track of the frontier.

## Topological Sorting

Complexity: O(m+n)  
Dependency: Depth-First-Search  
Terms to note: DAG - Directed acyclic (mean no cycles) graph  

Algorithm:
- By recursion: Kahn's method. It relies on a not-so-straightforward "Find nodes that have no incoming edges" utility and recurses on the subgraph of the original graph with the said no-incoming nodes removed.

![](http://2.bp.blogspot.com/-uuJn6FwwFAQ/U_njMhKdZ9I/AAAAAAAANmc/L07MfjJFkRA/s1600/TopologicalSort.png)

- By DFS: do DFS on all unexplored nodes, mark nodes that visited as explored. When encountering dead end nodes, i.e. nodes that have no outgoing edges which are unexplored or not existed, put it to the beginning of the sorted list. The algorithm terminates when all nodes are explored and sorted. Its methodology is kind of traversing to the end of the path, put the end node to sorted list and roll back to the preceeding node, check whether it is dead end, put it to the sorted list or if it branches to another path, following that path to the end and put it to the list. In the process of putting nodes to sorted list, we mark them as explored and treat any edge lead to them as dead end.

![](http://www.crazyforcode.com/wp-content/uploads/2016/04/DFS.png)

Application:
- Sort software packages by their dependencies during installation

## Kosaraju's Strongly Connected Components Detection

SCC: strongly connected component, a set of nodes in which we can travel from any node to any other node.  
Complexity: O(m+n)  
Dependency: Depth-First-Search  

Applications:
- Analyze network weaknesses or structure
- Analyze social networks, discover groups that are more closely connected (family, college alumni, coworkers, etc.)
- Analyze physical networks, discover regions that are more likely to be isolated in case of emergency.

Algorithm: [code here](kosaraju.py)
- Reverse the direction of all edges, call the new graph G<sup>rev</sup>
- Do first-pass DFS on G<sup>rev</sup>, similar to topological sorting. The purpose is to find an oder where nodes are moving upstream if followed. Prof. Tim calls it finishing time, i.e. which nodes finished first during the DFS.
- Use the just found upstream order and do a second DFS **by this order (lowest finishing time value first in G<sup>rev</sup> or upmost / most forward nodes first in G) on the original, unreversed graph G**, i.e. doing DFS from the most upstream nodes down to the most downstream. On respecting this order, the DFS-s are restricted terminated to any strongly-connected component (mean cycle) in the **upstream only** without the risk of wandering into downstream components. Everytime the DFS stops, an SCC is revealed. After that we restart the DFS on the unexplored, lowest finishing time node. The strongly connected components should be gradually discovered sequentially from the upstream down.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Kosaraju_example.PNG)

## Karger's min-cut algorithm
Reference: [here](https://en.wikipedia.org/wiki/Karger%27s_algorithm)

Code: [here](min_cut.py)

Complexity: O(m) for the contraction algorithm, O(n<sup>2</sup>mlogn) for running Karger's min-cut to guarantee an acceptable failure ratio (1/n).

Problem: find the minimum cut of a graph that divides it into 2 non-empty sets. The value of a cut is determined by the edges that connect the 2 partitioned sets.

This algorithm really raises the role of randomization in algorithm design. The rationale is when you seem not able to find an efficient solution (in polynomial time), you chance it by randomly select the solution. By random, it means with a tactic that employs randomization, certainly.

The brute-force approach takes O(2<sup>n</sup>) by taking all possible combinations of any 2 sets. The Karger's algorithm suggests a better success probability of 1/n<sup>2</sup> by probability analysis, which translates into an O(n<sup>2</sup>mlogn) complexity in time algorithm by running the contraction algorithm n<sup>2</sup>logn times, each has complexity of O(m) (best known possible solution, others include O(mlogm) and O(n<sup>2</sup>)).

In practice, the smallest cut can be obtained much earlier than the theoretical number n<sup>2</sup>logn. Probably due to the distribution of the result itself: if we run large enough number of iterations, good cut or even best cut can be encountered throughout the process, probably in the beginning. And we only need it once. Note that there is a relation between number of runs and expected success ratio: there is always a probability, though low, to find the smallest cut in the initial runs. The catch is: we may not be aware that is the smallest cut, how can we anyway. 

**In some simulations (running and count success cases so far, testing with graph size of 200 nodes and 50 nodes), I consistently found that the success ratio is around 2%, having smallest cut in only a few hundred repetitions. Cool! Randomization to the rescue, friends!**

Algorithm:
- Repeatedly run (n<sup>2</sup>logn) times contraction algorithm on the original graph
	- Randomly select an edge of all the available edges
	- Contract or collapse the 2 vertices of the selected edge:
		+ Create a new node representing the contracted vertices
		+ Transfer all the external (connecting to a third node) connections of the old nodes to the new nodes
		+ Remove all internal or self-loop (connecting the two contracted nodes) edges of the old nodes.
	- Stop when there are 2 vertices remained.
	- The cut value is obtained by counting the remained edges in the graph.
- Keep track of the smallest cut obtained so far


## Quick sort

New presentation in Divide-And-Conquer fashion:
- Divide: 
	* Choose pivot
	* Do swapping, ensure that at the end of the swapping, the selected pivot value will stay in its rightful place in the desired, sorted array. This is the new insight!
	* Pivoting process means that we do re-arrangement around the pivot value, not the pivot index. Hence the value selected as pivot will actually be moved around during the process.
- Conquer:
	* Sort left
	* Sort right
- Combine: since the process is in-place, there is practically a stand-alone combination.

**New insight: rigorous and mathematically proven technique** to choose pivot by Prof. Roughgarden: always choose the item in the first index as pivot value. The partition routine always assume that (pivot at the beginning of array) to do the partitioning. The tip here is before the partition process, swap WHATEVER value chosen as pivot TO the first index of the array (or sub-arrays). Randomization is introduced into pivot selection by simply guesing the median from [first, mid and last] trio items, which takes O(n).

**Another insight**: randomization is applied in this algorithm, however the randomness is not in the input data, but rather in the choice of pivot. AND amazingly, throughout the sorting process of one single input, numerous selections of pivot were made. Hence if averaged out, it pretty much centers around the median value, according to the law of large number, normal distribution. Which translates to the fact that more often than not the random choice of pivot is close to the median. Truly amazing and elegant in the way randomization comes into play here.

## Select k-th smallest item in an array

Complexity: O(n) with randomization.

This algorithm is analogous to quicksort, in the way that it utilizes the partition process and only recurse on one of the sub-arrays, depending on the relation between the returned pivot index and **k**. It is efficient in the sense that given an array of arbitrary size, it takes only linear time to pick the k-th smallest or largest item in the array. Another application, it takes only O(n) to get the median value. 

How is it possible? Think about the fact that it eliminates the boiler plate steps and only focuses on the k fraction of the recursed arrays. It does not care about statistic order in each of the sub-arrays. Its interest is simple and efficient: after each recursion, a large number of unnecessary data is thrown away in the left or right sub-arrays, depending on their size.


## Karatsuba's algorithm for efficient number multiplication

![Images](http://img2016.itdadao.com/d/file/tech/2016/10/22/cd310514221520581.jpg)

O(n<sup>log<sub>2</sub>3</sup>)~O(n<sup>1.585</sup>) time complexity as opposed to O(n<sup>2</sup>) in classical elementary multiplication algorithms.

## Find inversions in an array

Code: [here](find_inversions.py)

Brute-force: O(n<sup>2</sup>)

Good solution: O(nlogn), similar to merge sort. It is actually piggied back on merge sorting, where in merging / combine step, we add an extra step which is counting the number of inversion splitted between left and right arrays. The count starts whenever the merged array takes in data from the right array (which mean there is an inversion). The key point is that if i-th item from the left array is larger than j-ith item from the right array, all items above i-th are larger than j-th item as well. The counter should then add (ni - i) number of pairs to itself (pairs formed by [i ... ni] and [j] items).


Applications: [HackerRank challenge](https://www.hackerrank.com/challenges/new-year-chaos)

## Closest pair

Brute-force: O(n<sup>2</sup>)

Algorithm for O(nlogn):

![](https://i.stack.imgur.com/kIci0.png)

- Preprocessing: sort the data points in x to get Px, in y to get Py. Both contains the same data points, but in different orders.
- Divide: partition to left and right data points
	+ Take the index (n/2 where n is Px length) of the mid item in Px, get its x coordinate, name it x*, Px<sup>n+1</sup> will have the items from Px[0 ... n/2] on the left and Px[n/2+1 ... n] on the right
	+ Filter Py by x_bar: iterating from bottom to top in Py, if items have x coordinate less than x*, put it in Py<sup>n+1</sup><sub>left</sub>, otherwise in the right bucket Py<sup>n+1</sup><sub>right</sub>. By iterating from bottom to top, we preserve the y-increasing order. This is crucial!
	+ NOTE: Px<sup>n+1</sup> and Py<sup>n+1</sup> now MAY not contain the same data points (differ by the duplicated data points, in the event that duplicated data points (in x coordinate) occur. But the algorithm would, surprisingly, still WORK!
	+ The stop-check must be placed in the conquer step should left or right bucket Py be empty.
- Conquer: easy by recurrence.
	+ Left bucket: recursive call on (Px<sub>left</sub>, Py<sub>left</sub>)
	+ Right bucket: recursive call on (Px<sub>right</sub>, Py<sub>right</sub>)
	+ Split:
		- Compute delta = min(result from left, result from right)
		- Filter points within delta stride [x* - delta, x* + delta] ON Py set
		- Check each point in the stride with the next 7 points, which assures closest pair would be found if happens.
- Combine: if closer distance is found in split check, return it, other wise return the smaller result from left and right.

Formal solution: let's see first if I correctly understood your question. I will review the whole algorithm to make sure I don't give anything for granted. If you are confident you completely understand the algorithm and are just wondering why we used Py or Px, feel free to jump to point 7.

1. We have all our points in an array P. We create two arrays, sorting the points by coordinate x resulting in Px, and by coordinate y resulting in Py.

2. To use Divide and Conquer, we split all the points in two arrays. To split the points, we do it based on the x coordinate. This way, we create an array Q with all the points present on the left half of Px, and an array R with the points of the right half of Px.

3. With recursion we compute the closest pair of points in Q, and the closest pair of points in R. The shortest distance of both of them will be our δ
So far so good, right? We still have to check the closest pair with one point in Q and the other point in R, which is the tricky part.

4. Now we define x¯ as the biggest x coordinate of any point in Q. The value of x¯ is the frontier between the points of Q and the points of R.

5. Recalling what δ was, we are confident that, if the closest pair has one point in each side, they have to be as distant as δ to be the closest pair of P (all the points). If this pair was further than δ, that would mean that the closest pair of P was the pair we used to define δ.

6. Taking into account points 4. and 5., makes sense to focus only of those points with its x coordinate in the range x¯−δ,x¯+δ. We will create an array S with the points that satisfy the x coordinate limit that we just established. How do we construct S?

7. We aim to get the closestSplitPair in linear time, and I think this is the key to answer your question. How many points will we have at S? We don't know. In fact S could have as many points as P! To solve it in linear time we cannot afford to compare each possible pair. This would take O(n2) time. What can we do? We can compare each point of S only with other points with an y coordinate difference of at most δ. But to do so we need S sorted by y coordinate. We could filter Px based in point 6 limitations and sort S by y coordinate, but this would take O(nlog(n)) time, not linear. However, there is a trick we can do to have the points in S sorted by y coordinate in linear time. And this is the main reason we created Px and Py in the first place. We can just run through Py and if the current point satisfies the limitations of point 6, we store that point in S. This way we get the points sorted by y coordinate in linear time!

8. Even this way, we cannot assure that there will be several points in S that falls in the same y,y+δ range. Or can we? In fact, we can. Given that δ was the closest pair of points in the same side of x¯, we are sure that there will be no points at the same half closer than δ. Therefore if we draw the know δ∗2δ rectangle, we can easily prove that at most we will have 8 points inside the rectangle. Therefore we will only need to compare each point in S with the next 7 points ordered by y coordinate. In fact we can prove that there will be needed just 5 comparisons, although the prove is not as easy. Feel free to investigate about that.

## GCD and LCM, a.k.a Greatest Common Divisor and Least Common Multiplier

At last, I collected the technique to find common divisors and multipliers. It is an addition to my algorithm toolbox , a very simple, fundamental yet very elegant and satisfactory. It draws a fine and definite line between a computer scientist and a monkey coder, or ones with algorithm understanding and those without.

The GCD and LCM relates by this formula: lcm(a, b) = a x b / gcd(a, b)

The gcd can be found using different techniques, namely prime factorization, binary factorization. I chose Euclidean thanks to its simplicity. Asymtotically it does not differ a lot from the most efficient methods.

Look at this simple algorithm!  
Complexity: O(logn) on average, O(h) in worst-case scenarios where h is the number of digits in the smaller number. Further [here](https://stackoverflow.com/questions/3980416/time-complexity-of-euclids-algorithm).
```javascript
gcd(a, b):
	if a === b:
		return a
	else if a > b:
		return gcd(a-b, b)
	else:
		return gcd(b-a, a)

lcm(a, b):
	return a / gcd(a, b) * b // doing the division before multiplying by b (assuming a is larger) can be beneficial to memory storage
```
Recursively replacing the larger number with the difference. An improvement can be made by using the remainder in lieu of the difference.

Advanced and further readings: 
- [Euclidean Method](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [Binary GCD Algorithm](https://en.wikipedia.org/wiki/Binary_GCD_algorithm)
- [Prime Factorization](https://en.wikipedia.org/wiki/Integer_factorization)

## Resources:

- CLRS - Cormen, Leiserson, Rivest, and Stein, Introduction to Algorithms (3rd edition)
- DPV - Dasgupta, Papadimitriou, and Vazirani, Algorithms
- KT - Kleinberg and Tardos, Algorithm Design
- SW  - Sedgewick and Wayne, Algorithms (4th edition)
