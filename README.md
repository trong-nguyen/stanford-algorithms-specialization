# Algorithms Specialization, Stanford - Coursera courses

This repo houses all of the projects that I extensively studied, completed and documented for the Stanford - Coursera Specialization on algorithms by Prof. Tim Roughgarden. The curriculum is substantial and provides a great deal of information from essential techniques such as efficient sorting, to fundamental data structures, to graph theory, divide and conquer, dynamic programming, and even an overview of difficult np-complete / np-hard problems. The whole specialization, which comprises 4 courses and took me 3 months, solidified my computer science knowledge. The courses really pushed me hard, but I feel acomplished and enlightened on the day of completion.


School: Coursera
Class: Algorithms Divide and Conquer
Lecturer: Tim Roughgarden - Professor at Stanford University
Published: 2012

# Who are you?

![Imgur](http://i.imgur.com/c7uj0T1.png)

I was at level 1. Now 1.5. Pushing myself to level 2.

# Algorithm Design And Analysis
Algorithms use one or more of the following methods:
- Divide and conquer
Sorting algorithms (merge, quick)
- Randomized algorithms
Quick sort
- Dynamic programming: the solutions to subproblems are mostly similar, hence can be reused to tremendously speedup computation. The term dynamic programming is closer to data tabulation than to programming due to a historial reason.
	+ Max-weight independent set (textbook problem)
	+ Fractional knapsack problem
- Greedy method: relies on the **local** optimal subtructure property of the problem.
	+ Dijkstras's method
	+ Activity selection
	+ Huffman encoding algorithm
	+ 0-1 (binary) Knapsack problem

### Dynamic programming ingredients:
1) the problems can be divided into finite sub-problems.
2) the solution to the upper-problem depends on the solutions to the sub-problems in a simple expression (think max, min, add ...)
3) the original solution is the so
lution to the subproblem of the biggest size within the boundary (space) of the original problem.

### Dynamic programming vs Divide and Conquer:
Similar to divide and conquer, the original problem can be divided into subproblems. However, unlike divide and conquer, where the solutions to sub-problems are clear-cut (think merging) or relatively separated (think in finding smallest-distance pair, we only need to consider a small region where the subproblems relate, to be exact 2*δx), the subproblems in dynamic programming intertwine, where some or most of the solution to this subproblem is present in another (think 50% in independent set problem). Hence if there is a technique (memoization) that can save the solutions of subproblems, tremendous speedup is achievable (eg. exponential to linear in max-weight independent set problem).


### Dynamic programming vs Greedy method:
Algorithms that use greedy method differ from those using dynamic programming in the following ways:
- In dynamic programming, the solution to a problem depends on the solution to its subproblem. While in greedy method, the solution only depends on the information local to that paticular subproblem. This results in the following consequence.
- Dynamic programming uses bottom-up approach, greedy method uses top-down.

## NP vs P - Super High Level Thinking About Decision Algorithms

[Good Reference Articles (3 Parts)](https://cs.stackexchange.com/a/9566)

**P**: polynomial time **SOLVABLE** problems

**NP**: Non-deterministic Polynomial time problems, polynomial time **VERIFIABLE** problems.
Facts:
- P is a subset (or identical set) of NP.
- All NP problems can be solved by brute-force search in exponential time.

The definition of NP problems can be expressed in input - output definition:
- Input size is expressible in polynomial terms.
- Solutions / certificates can be verified in polynomial time.

**NP-complete**: a subset of NP problems that contain the hardest ones within it. All NP-complete problems are at least as hard as any NP problem.

A recipe for solving an NP-complete problem X:
- Find a known NP-complete problem A
- Prove that X reduces to A which implies:
	+ A at least as hard as X
	+ A is an NP-complete problem

A more practical recipe:
1. Try to solve special cases (tractable) of the problem. For ex. in the case of vertex cover:
	+ Solve the problem for trees instead of generic graphs
	+ Solve for bipartite
	+ Solve when the solution is small, like logn, (so that we can guess since the pool is small / brute-force is feasible)
2. Apply heuristic conditions (use approximations): min-cut.
3. Find a better solution which is `poly < solution < brute-force`

**NP-hard**: Hardest problems of all, not solvable nor verifiable in polynomial time.

Right now there are 3 potential answers to the NP vs P question. Note that P ⊆ NP [(proof)](https://stackoverflow.com/a/2639634):
- NP = P (and so is NP-complete)
- NP ≠ P (and hence P ⊂ NP)
- NP is not = nor ≠ P (since the question is wrong)

Super-roughly speaking in set theory language: **P ≤ NP ≤ NP-complete < NP-hard**.

![](http://slideplayer.com/677302/1/images/6/NP+P+NP-hard+NP-complete.jpg)

The fact that an NP-complete problem is **at least** as hard as any NP problem suggests that once we can solve a single problem of NP-complete category in polynomial time, we can achieve polynomial time solutions for all NP problems. That is why trying to solve an NP-complete problem in polynomial time (or prove that it is impossible) is of tremendous interest in computer science. It will open (or close for good) the door for algorithm research (if we can solve our problem efficiently, you can solve yours for sure since it was proven that the upper bound of difficulty is the same). It is like once we beat the boss, other monsters are just at most as difficult.

Another fact is that over the last decades, despite intensive research of all kinds of algorithm, none was found for NP-complete problem that is polynomial-time. This doesnot neccessarily confirm the non-existence of such efficient algorithms, but somehow tips the scale towards the NP ≠ P, making it the more probable answer! (there are polls among researchers that increasingly favor the NP ≠ P)

### Takeaway - the point of studying / categorizing problems based on NP-difficulty is:
#### - To realize whether a problem is NP
#### - Be realistic and not to expect polynomial time solutions and aim to something though not as good as polynomial but not quite bad as brute-force solutions (could be 2<sup>n</sup>, `n!`).
#### - To be intellectually and mentally prepared when designing algorithms since you already know there is potentially a wall / roadblock / bottleneck and expect a detour (probably longer than polynomial).



## Data Structures
### Heap
Synonymn: `priority queue`

Complexity: O(logn) for basic operations.

![Imgur](http://i.imgur.com/luBB8J8.png)

Fundamental operations:
- Insertion
- ExtractMin (or equiv. ExtractMax)

Usecases: if we see problems involved sorting as static problems, i.e. we need a definite solution at the end of a process, then heaps are perfectly suitable for dynamic problems. That means problems increasing size over the time and we need a simple information at each timestep, e.g. `min` or `max` values or something that can be cleverly inferred from `min and max` - see application 2.



**Applications**:

![Imgur](http://i.imgur.com/yW2zi3u.png)

**Heap vs Binary Search Tree**:
- Heap: parent's values are always smaller than or equal to children's values.

![Heap](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Min-heap.png/240px-Min-heap.png)

- Binary Search Tree: parent's values are larger than all values in the left subtree but smaller than those in the right subtree.

![BST](https://www.tutorialspoint.com/data_structures_algorithms/images/binary_search_tree.jpg)

### Balanced Binary Search Tree

Balanced binary search trees, either height- or weight- balanced, are analogous to geometry similarity, search trees could be thought of as quadrilaterals, while red black and AVL (Russian, abbr.) are rectangulars and perfectly balanced search trees are squares. It always come with the cost: nicer features lead to higher maintenance cost, i.e. more complicated to maintain the structure / invariants (red-black invariants or 1-leveled depth difference in AVL).

| Operation / Structure | BBST (red-black)    | BST     | Heap    | Hash Table | Bloom Filter |
| --------------------- | ------------------- | ------- | ------- | ---------- | ---------- |
| Search         		| O(logn)             | O(logn) |         | O(1) 	   | O(1)       |
| Select         		| O(logn)             | O(1) 	| O(n)    | O(n) 	   |            |
| Min / Max         	| O(logn)             | O(1) 	| O(1)    |            |            |
| Pred / Succ         	| O(logn)             | O(1) 	|         |   	 	   |            |
| Rank         			| O(logn)             | O(logn) |         |   	 	   |            |
| Output in sorted order| O(n) 	              | O(n) 	|         |   	 	   |            |
| Insert         		| O(logn)             | O(n) 	| O(logn) | O(1) 	   | O(1)       |
| Delete         		| O(logn)             | O(n) 	| O(logn) | O(1) 	   |            |


![Imgur](http://i.imgur.com/y1zYnZm.png)

**Red-Black Tree**:
- The whole point is to have a balanced tree, i.e. trees that guarantee heights of O(logn) hence ensure efficient operations. There is no additional fancy thing about the red-black trees in terms of features. **They are just binary search tree with better performance**.
- Insertions mostly will introduce red nodes, readjustments (to maintain the invariants) will introduce black ones. That is how the number of red and black nodes are roughly in the same order.
- Every insertion operation includes 2 phases: positioning (standard binary search tree insertion, e.g. end-insertion, rotations, bubling up, etc.) and color coding (e.g. red coloring then readjusting)
- Readjustment: insert the new node as red node and bubble up if invariants are violated (two red in a row). Might involve rotations to increase efficiency.

![](http://www.geeksforgeeks.org/wp-content/uploads/redBlackCase2.png)

**AVL Tree**:
[Reference](https://stackoverflow.com/a/28846533)

- insert: RB tree & avl tree has constant number of max rotation but RB tree will be faster because on average RB tree use less rotation.

- lookup: AVL tree is faster, because AVL tree has less depth.

- delete: RB tree has constant number of max rotation but AVL tree can have O(log N) times of rotation as worst. and on average RB tree also has less number of rotation thus RB tree is faster.

For large data (millions):

- insert: AVL tree is faster. because you need to lookup for a particular node before insertion. as you have more data the time difference on looking up the particular node grows proportional to O(log N). but AVL tree & RB tree still only need constant number of rotation at the worst case. Thus the bottle neck will become the time you lookup for that particular node.

- lookup: AVL tree is faster. (same as in small data case)

- delete: AVL tree is faster on average, but in worst case RB tree is faster. because you also need to lookup for a very deep node to swap before removal (similar to the reason of insertion). on average both trees has constant number of rotation. but RB tree has a constant upper bound for rotation.

### Hash Table

Operations: O(1) complexity for the following operations

- Insert
- Delete
- Lookup

**Collisons** are prevalent and should be premptively addressed. There are 2 strategies:
- Chaining: put collided hashed items into a linked list. h(k1) = h(k2) = x, bucket x contains [(k1, v1) -> (k2, v2) -> ...] where v1, v2, ... are sattelite values. Suitable for cramped items, i.e. number of items > number of buckets.
- Open addressing: or probing. Apply sequentially a number of hash functions: h1(k) = x1 occupied? => h2(k) = x2 occupied? => ... Basically this method tries to find an unoccupied bucket for the collided hashed values, **not applicable to cramped items, only where number of items << number of buckets.
- Pathodological datasets: fixed a hashing function h(k) (no matter how clever it is) there always exist a dataset underwhich the hash function will perform as bad as the most miserable hash function. This is due to the compression step (from a big universe to a small set) during the hashing process. Which exactly gave rise to the class of universal hashing functions
- Universal hashing functions: randomly selected any function h(k) belongs to the universal class H, the probability of a colission of 2 random keys x and y **is as good as a random function, which is 1/n**.
	+ Universal hash functions (UHF) with chaning hash tables **guarantees** that all operations (insert/delete/lookup) are O(1)
	+ UHF with open addressing: guarantees the insertion time of 1/(1-α)
	+ UHF with linear probing: insertion time is 1/(1-α)<sup>2</sup>

**A good hash table has**:
- Controlled load factor (number of items / number of buckets)
- Good hash function which in turn depends on:
	+ Golden standard: simple uniform hashing, every key is likely equal to hash to any of the bucket.
	+ In case of the multiplication / division hashing methods, the divisor or multiplier should be the closest prime number to the number of buckets to avoid biases.
	+ Qualitative: easy to store, easy to evaluate
	+ **More art than science**!
	+ Randomized >< Deterministic


![Imgur](http://i.imgur.com/i8tPQBH.png)

### Bloom Filter

Complexity: O(1) for insert and lookup, no deletion, comes with false positive probability (report an item inserted when it was not).

Formulae:
- False positive probability ~ (1-e<sup>-k/b</sup>)<sup>k</sup>
- Optimal number of hash functions k = ln2 x b = 0.693b
- False positive probability given optimal k: (1/2)<sup>(ln2)b</sup>

**Bloom Filter vs Hash Table**:

Pros: more space efficient
Cons: can't store associated data, no deletions, suffering from a small false positive probability.

![Imgur](http://i.imgur.com/Ebyrqh5.png)

## SUM-2 Problem - A clever application of binary search and hash table
Problem: given an array A of size n, find all item pair that sum up to a given value t.

Hash table solution:
- Save all items in the array to a hash table: O(n)
- For each item x, look up the value y = t - x: n operations each of O(1) -> O(n).
Complexity: O(n)

Binary search solution:
- Sort the array: O(nlogn)
- For each item x, search for the value y = t - x: n operations each of O(logn) -> O(nlogn).
Complexity: O(nlogn)

**Advanced problem**: same as the original SUM-2 but now we need to find all item pair that sum up to one of the value in a range of value t[low:high] of size m.

Analogously, the hash table solution is O(n*m) and the binary search solution O(mnlogn).

However a tweak on the binary search solution gives surprisingly good performance compared to the hash table.

Modified binary search solution, [code here](sum2.py):
- Sort the array: O(nlogn)
- For each item x, locate the range in A that contains the admissible y where (x+y) falls in [t<sub>low</sub> ... t<sub>high</sub>] as follow:
	+ we need t<sub>low</sub> < x + y < t<sub>high</sub>, hence t<sub>low</sub> - x < y < t<sub>high</sub> - x
	+ Let's call this range [i:j], which contain items y<sub>i</sub> ... y<sub>j</sub> where y<sub>k</sub> = A<sub>k</sub>. This step takes 2logn (thanks to the binary search) operations per item x.
	+ We can add x to y[i...j] to obtain t[i...j], the corresponding values y for x. Statistically, let's assume t[i...j] has average length of c.
	+ Collectively, the whole step is O(nlogn).
- From step 2, we obtain a list of T<sub>0</sub>, T<sub>1</sub>, .... T<sub>n-1</sub>, where each T is a subset of T<sup>*</sup>=[t<sub>low</sub> ... t<sub>high</sub>]. The cost to count distinct values t<sub>i</sub> of all T<sub>i</sub> is O(nclog(nc)) ~ O(nclog(n)) since `c <= m = O(n)` hence `O(log(nc))` = `O(log(n))`, where c is the average lenght of the admissible sublists. The cost might be reduced O(nc) if we use a hash table for marking the t<sub>i</sub> that was summed up by any found (x,y) pair.

All in all it takes: O(nlogn) for sorting, O(nlogn) for finding admissible range, and O(nclog(n)). Total complexity: **O(nclogn)**.

Hence, the decision of using hash table or binary search structures boils down to the relative magnitude of `m/logn` and `c`. When the admissible arrays are sparse, meaning there are few item pairs that sum up to the interested values, c is small compared to m and logn is relatively small also which might lead to a much faster performance when using binary search. Practically, the hash table solution is inferior until c approaches the value of `m/log(n)`

For example: in Prof. Roughgarden's assignment, n = 1 million, m is 20000, logn ~ 20. Theoretically, binary search is better before c reaches `m/logn` ~ 1000. In the scope of this paticular problem, c was found to be less than 10 and hence the binary search is 2 orders faster than hash tables. It literally translates to seconds versus hours performance.

The takeaway is, again, we should by all mean exploit the boundary conditions. In this case, instead of paying the whole price of m lookups for each item, it is possible to narrow down to `c` lookups (and pay a premium of `logn` to combine/eliminate duplicates), which is much much better!

'''python
There are 427 summable values in range (-10000, 10000)
There are 4274 summable values in range (-100000, 100000)
There are 42760 summable values in range (-1000000, 1000000)
There are 427657 summable values in range (-10000000, 10000000)
[Finished in 138.6s]
'''

## Knapsack Problem - Dynamic Programming
Complexity: O(nW) where n is the number of items and W is the weight constraint on knapped items.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Knapsack.svg/250px-Knapsack.svg.png)
![](https://i.ytimg.com/vi/mZccw_6hOGU/maxresdefault.jpg)
K here is the same as table A in the explanation.

**Problem**: given a number of items with corresponding value v<sub>i</sub>	and weight w<sub>i</sub>. Find a subset S that maximizes the accumulated item value subjected to total weight constraint W.

Utilizing the local optimal substructure that an item i-th is either belonging to the optimal set S or not. When it is, we work on the subproblem with new weight constraint W-w<sub>i</sub> and added value v<sub>i</sub>. When it is not, we work on the subproblem with item i-th excluded.

**Algorithm**: [code](./knapsack.py)

Bottom up approach with iterations:
Finding optimal values step: form a 2D-array with n columns representing the selection of item i-th and W rows representing the optimal values selected at weight limit w<sub>j</sub>.
- Fill zeros into colum 0, implying there is no value could be knapped with 0 item selected.
- At column i and weight j, the optimal value is a) either inherited from column [i-1, <sub>j</sub>] meaning the optimal value when item i not considered is still optimal when it is, OR b) the sum of the value v<sub>i</sub> and the prior optimal value of the sub problem [i-1, W-w<sub>i</sub>], depending on which one has the larger value.
- The value at column i-th and row-j is the optimal value of the knapsack problem when items from 1 to i-th considered and the total weight is limited by w<sub>j</sub>.

Top down approach with recursions: starting at the desired level of n items and weights limit W, we ask the question: what do we need to compute this value. Using the same matrix from the bottom approach, we actually need the left [i-1:W] and [i-1:W-w] values. Recursion on the subproblems with those new limits lead to deeper recursions to solve our problem. Interestingly, it is also found that this approach helps skip a lot of unncessary levels of w, precisely between [w:W], i.e. {w+1, w+2 ..., W-1}. The larger the weights of items w<sub>i</sub> with respect to weight limits W, the more computational cost we save.

Retrieval step: the following retrieval steps can succeed both top down and bottom up approach to find the actual knapsack items. It is indeed very similar to the top down approach, except that the necessary values has been known. Using either matrix A or hash table A in the finding step to retrieve the actual items that have been knapped in the optimal set S.
- Starting from column n-th and row W, the optimal value for the orignal Knapsack problem [n, W], we determine to whether or not item i-th was included.
- To find out, we need to track where the value at cell [i,j] came from. If its value was inherited from the adjacent left column A[i,j] = A[i-1,j] then item i-th was not included. Otherwise if A[i,j] = A[i-1, j-w<sub>i</sub>], then it was included.
- Repeat the process until we hit the the zero residue, meaning all items included in the optimal set were accounted for.

## Sequence Alignment - Dynamic Programming
**Complexity**: O(nm) where n and m are the length of to be aligned strings, respectively.

![](https://upload.wikimedia.org/wikipedia/commons/3/3f/Needleman-Wunsch_pairwise_sequence_alignment.png)

**Problem**: Given 2 strings x and y, find the alignment which minimize the penalty due to mismatched and gaps insertion. Gaps are allowed to insert into the original strings to facilitate the alignment. Example: the alignment for string abcd and ace would be: abcd and a_ce, and the penalty would be 2 due to 1 gap inserted and 1 mismatch (d and e), presume that mismatch penalty = gap penalty = 1.

**Algorithm**: [code](./sequence_alignment.py)
This algorithm is amazing. It is almost impossibly hard to fathom the solution without applying dynamic programming.

Calculating minimized penalty step:
- Form a n+1 by m+1 matrix where n and m are lengths of string x and y, in that order. The first column and row are for empty match, i.e. string x matches 0 characters of string y and vice versa.
- Fill in the column 0 and row 0 with gap penalties. The value at cell i,j is the minimal penalty of matching sub-strings x[0:i] and y[0:j].
```python
A[i][0] = i * gap_penalty
A[0][j] = j * gap_penalty
```
- At subsequent cells i, j where i, j >= 1: there are 3 possibilities to account for:
```python
A[i][j] = min(
	penalty(x[i], y[j]) + A[i-1][j-1], #penalty = 0 if characters match (x[i] = y[j]) or mismatch_penalty otherwise
	gap_penalty + A[i-1][j], #we insert a gap and assume the penalty of the gap plus the minimal penalty of the sub problem (x[0:i-1] and y[0:j]), i.e. peel off one letter of the substring x[0:i]
	gap_penalty + A[i][j-1] #similar to case 2 we insert a gap and assume the penalty of the gap plus the minimal penalty of the sub problem (x[0:i] and y[0:j-1]), i.e. peel off one letter of the substring y[0:j]
)
```

Retrieval step:
- Starting from the furthest cell i=m, j=n
- Compute the values of the 3 possibilities which might lead to the value at cell i, j
```python
p1 = penalty(x[i], y[j]) + A[i-1][j-1]
p2 = gap_penalty + A[i-1][j]
p3 = gap_penalty + A[i][j-1]
if:
	A[i][j] == p1: # no_gap_inserted, characters i and j might match or not
		i -= 1, j -= 1
	A[i][j] == p2: # gap_inserted_in_y
		i -= 1
	A[i][j] == p3: # gap_inserted_in_x
		j -= 1
```
- Repeat until all characters exhausted, i = 0 and j = 0

Example: align string
* x = lkasdfoiu2098374kjhsdlfkup29834hsakfdjh9823
* y = kalshjfdpoiuer987123hfskdjlhfliuasyf98234
```
Matching pattern costs [32/44] penalty, () and _ mean mismatched and gap insertion, respectively:
	(_;)l(_kas)d(f)oiu(20)98(3)7(4kj)h(sdl)f(kup29834hs)a(kfdjh)9823(_)
	(ka)l(shjf)d(p)oiu(er)98(_)7(123)h(___)f(skdjlhfliu)a(__syf)9823(4)
```

## Optimal Binary Search Tree - Dynamic Programming
**Complexity**: O(n<sup>2</sup>) with Knuth's optimization technique

![](http://slideplayer.com/6825567/23/images/5/Optimal+Binary+Search+Tree.jpg)
![](http://www.readorrefer.in/media/extra/zqpivcU.jpg)


**Problem**: building an optimal binary search tree with minimal search cost, given search probabilities of all items. The solution for this problem is a step up in applying dynamic programming paradigm, when the possibilities to consider in the innermost loop - the substructure - is of O(n) instead of O(1) in knapsack or sequence alignment problems.

**Algorithm**: [code](./bst.py) building a 2D array
- Working on upper half triangle of the matrix
- Cell i,j contains the optimal weighted search cost for problems with size from i to j inclusive.
- At each cell i, j, calculate cost of all the root possibilities in between [i:j] sum(p[i:j]) + C([i:r-1] + C([r+1:j]) where r is the test root index between i and j. Choose min value among all calculated cost with tested roots and  put it in cell i,j.
- The process is carried out diagonally and shifting upward when j moves from 0 to n
- The solution is at the final value A[1,n], representing the subproblem with size [1:n], which is also the original problem.

**Knuth's optimization technique**: observe that the tree root can only be located in between the subtree roots. Of all the possible sub tree roots, we grasp:
- the biggest possible left tree T1=[i:j-1], which means T = T1 + root + empty right subtree
- the biggest possible right tree T2=[i+1:j], which means T = empty left tree + root + T2.

From there, we can modify the innermost loop such that instead of scanning the cost of all possible subtrees having root from i to j, we only look at optimal roots ranges from the root of the sub trees [i,j-1] and [i+1, j], i.e. the subtrees obtained by peeling off one element on the left and right, respectively. This optimization requires maintaning a separate array of the optimal root index R where R<sub>i,j</sub> coressponds to the optimal root index of the sub problem [i:j].


**Tree Retrieval**: to retrieve the actual search tree, we use array R.
- The root node r1 is obtained from R[1,n], which translates to the optimal problem of size [1:n] or our original problem.
- From there we can deduce the left branch root left_root = R[1,r1-1] and right right_root = R[r1+1,n] only if the respective left/right subproblem is not empty.
- Recursively we then could obtain the entire tree.

Further reading:
- [Implementation guide](http://www.cs.duke.edu/courses/fall05/cps230/L-06.pdf)
- [Knuth's article](http://www.inrg.csie.ntu.edu.tw/algorithm2014/presentation/Knuth71.pdf)

## Huffman coding algorithm - Greedy
Complexity: O(nlogn) using heap or 2 queues. Code [here](huffman_encoding.py)

![](https://1.bp.blogspot.com/-IeNrHoXgn-0/VzgysPXhG3I/AAAAAAAAcrU/4IWDHf2IWCs8bDcd81WvcV3NCNNbFFCZwCLcB/s1600/huff.png)

Applications: used in MPEG3, JPEG media encoding (though partially)

The idea is based on the local optimal substructure: the two least frequent symbols can be optimally replaced by a merged node with one of the leaf has label 0 and the other 1. The process if iteratively carried out minimize the expected Σ(pi x li) where li is the length (in terms of bits) of the encoded symbol.

![](http://collegelabs.co/clabs/nld/images/huffman_final.gif)

Algorithm: using 2 queues to sequentially build the binary tree with leaves the encoded symbols.
- Presorting the vertices by their weights and put them to queue 1
- Initialize queue 2 with zero item. This queue will take in merged vertices.
- While there is more than 1 node in both queues:
	+ Pop the 2 smallest weight items of the 2 queues. They can be both from queue 1 or queue 2 or in either.
	+ Merge them and enqueue it to queue 2
	+ Could use a map to maintain the coded bit at that particular branch (accumulate later to get the complete code for that node)
- Stop when there are only 2 nodes remained in 2 queues. Merge them and name the merged node to be the root.

## Max Weight Independent Set - Dynamic Programming
Complexity: O(n)
![](https://upload.wikimedia.org/wikipedia/commons/b/bd/Mis_pathgraph_p3.png)

This is a astonishing illustration for the fact that: "more math requires less code and more code probably due to insufficient math". The algorithm is elegant and extremely simple for a problem appeared to be mind-bending at first. For a path graph with weights, or an array of weights, find a set of nodes that has the highest sum of weights, on the condition that no consecutive nodes are choosen. The brute force approach has to work on exponential number of possibilities (most of them repeated). On rigorous analysis and making use of dynamic programming paradigm, the possibilities are drastically reduced and a linear complexity can be achieved.

Algorithm: create an array A that has the same size as that of the weight array (W). At index i-th is the optimal accumulated weights for the subproblem, an array of size [0-i] with i node inclusive. To fill in values for array A, we use the bottom to top approach. The first and second values of array A are straightforward to compute, where A[0] = W[0] and A[1] = max(W[0], W[1]). For the third and beyond we have a recursive formula: A[i] = max(A[i-1], A[i-2] + W[i]). Array A gives accumulated maximal weights of array A[0-i] at each position. To retrieve which vertex were actually included in the set we can iterate from top to bottom. At index i-th, the vertex i-th is not included if A[i] is the same as A[i-1], and included if A[i] is larger than A[i-1], in which case we can skip vertex i-1 since it is the adjacent vertex.
```python
# bottom to top to fill in cache values A
def max_weight_set(weights):
	A = [0] * len(weights)
	A[0] = weights[0]
	A[1] = max(A[0], weights[1])
	for i in range(2, len(A)):
		A[i] = max(weights[i] + A[i-2], A[i-1])
	return A

# top to bottom to get the selected set
def retrieve_set(A):
	selected = [0] * len(A)
	i = len(A) - 1
	while i >= 1:
		if A[i] == A[i-1]:
			selected[i] = 0
			i -= 1
		else:
			selected[i] = 1
			i -= 2
	selected[0] = int(not selected[1])

	return selected
```

Advanced: max weight independent set applied to graph. The algorithm developed for a path graph can be applied efficiently and correctly to tree.

![](http://mathworld.wolfram.com/images/eps-gif/MaximumIndependentSet_1000.gif)

## Prim's Algorithm for Minimum Spanning Tree (MST) Problem
Complexity: O(mlogn) using heap

![](https://i.stack.imgur.com/KofyW.gif)

Foundation:
- Prim's algorithm guarantees to output a spanning tree (not neccessarily minimum): this in turn relies on:
	+ Empty cut property (zero cut <-> disconnected): guarantees the algorithm continues untill all vertices are included.
	+ Double-crossing cut property: assure no cycle produced since Prim's algorithm advances 1 edge at the time, and that edge has no loop back (thanks to the removal step after inclusion).
- **Cut Property**: if there exists a cut (A, B) of graph G and e is the cheapst crossing edge between A and B **THEN** e belongs to a MST (the MST if all costs are distinct) of G.

Algorithm: proceeding somehow similar to Dijkstra's algorithm:

- Take an arbitrary vertice v of G with an arbitrary node
- Add all edges with v as the endpoint to the heap (this is the frontier edges)
- Iterate through all edges in the heap and pop the one with lowest cost:
	+ if the edge loop back to one of the vertices in MST, ignore it
	+ if one end u of the edge lies outside of the MST, add it to the MST and add all edges associated to u (which is not already in the MST) to the heap
- Terminate when the MST fully spans graph G (has the same number of nodes as G's)

[Code here](prim_mst.py)
```python
v = arbitrary_vertice_from(G)
MST = {}
heap = heapify([(cost, (v, u)) for u, cost in G[v]])
while len(MST) != len(G) and heap:
	cost, edge = pop_min(heap) # pick the min cost edge
	if edge in MST: # both endpoints already in MST
		continue # discard and ignore
	u = old_node(edge) # the endpoint already in MST
	v = new_node(edge) # the one that is not

	MST[u][v] = MST[v][u] = cost

	for neighbor, cost in G[v] if neighbor not in MST:
		edge = (v, neighbor)
		add (cost, edge) to heap
```

Analysis: the iteration is at most m size since it does not visit any edge more than twice (first to push to the heap, and second to pop it). For each edge considered, it takes O(logn) to pop the min cost edge or push it to the heap. Though there is not a clear cut between heap poping and pushing, they intertwine (a few poping occur until a crossing edge found and then a few pushing to add connectivities of the new node to the heap) when we advance the frontier vertices. However, it will never take more than one poping and one pushing for an edge in total.

**Total: O(mlogn)**

## Dijkstra - Shortest path finding

References:
- [Dijkstra's algorithm on Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Applications](http://www.csl.mtu.edu/cs2321/www/newLectures/30_More_Dijkstra.htm)

![Imgur](http://i.imgur.com/f4M9f2F.png)

## Bellman - Ford shortest path finding - Dynamic Programming

Complexity: O(mn), applicable to graph with negative edges, but non-negative cycles. Distributed in nature, suitable for clustered computing.

Algorithm: take a budget-based point of view that given increasing number of hops `i` allowed, find shortest path from a source `s` to a destination `t`. The fact that the shortest path in a n vertices graph the shortest path is at most `n-1` length guarantees that the maximum number of hops we need to traverse from the source is capped at `n-1`. Basically we check all the paths from s to t and choose the shortest one, by brute-force. The local substructure optimality of the problem in which **the shortest path to t must either: of length (i-1) plus an edge through one of the predecessors of t (hence total length `i`) or already reach t at length (i-1)** suggests the use of dynamic programming. Notice the similarity to **Max-weight independent set** when we either choose A<sub>i-1</sub> or A<sub>i-2</sub> + w<sub>i</sub>. In fact this algorithm of Bellman-Ford relates to all of the previous dynamic programming problems, since it advances by looking and choosing between previous calculated values plus new results.

The whole algorithm is:
- Create a 2 dimensional array A<sub>i,v</sub> (where i is the current length allowed and v the iterating vertice) and init it with A<sub>i=0,v=s</sub> = 0.
- From i=0 to n-1, iterate over all v in the graph, compute A<sub>i,v</sub> = min(A<sub>inherited</sub>, A<sub>propagated</sub>) where:
	+ A<sub>inherited</sub> = A<sub>i-1,v</sub>
	+ A<sub>propagated</sub> = min(A<sub>i-1,w</sub> + c<sub>wv</sub>) of all predecessors w of v where c is the lenght from w to v
- The process terminates when `i = n-1` or A<sub>i,v</sub> = A<sub>i-1,v</sub> for every v (early stop, basically the values are stagnant)

The entire process is somewhat BFS-ish, advancing layers by layers, with extra work cost of `m` due to min evaluation among all calculated paths.

Examples:

![Imgur](http://i.imgur.com/L7cotkT.jpg)
*Values propagation*

![Imgur](http://i.imgur.com/deJ6Hlu.gif)
*With shortest path illustrated. Notice the A values (yellow filled circles) are initially infinite (except source) and gradually propagated downstream. The green highlighted path denotes the current shortest path found.*

Variations:
- Source - centric vs destination - centric: starting from source / destination and working towards destination / source.
- Pull update vs push update: in-progress vertices asking for values vs. updated vertex pushing values and ask neighbors to update route accordingly

Problems:
- "Counting to infinity": problems involve asynchrocy (autonomous computation), circular connections (one has 2 way-ed connection to another) and push-updating.
- Fix to the "counting to infinity": path vector protocol: each node saves the entire path from itself to the destination, this is essentially the reconstruction problem.

Application: Internet routing

## Floy-Warshall All Pair Shortest Path Finding - Dynamic Programming
Problem: find the shortest path between all pairs in a graph with negative edges.

Complexity: O(n<sup>3</sup>).

Algorithm: the solution is actually quite simple. The key is figure out the common works and utilize that work in the actual computation process. There are 2 aspects to understand the algorithm:
- The mechanism: there is a metaphor to easier understand the rationale by asking this question: **to find the shortest path from i-j, I would ask every node k in the graph: what is the cost from you (`k`) to `j`, then I would choose the `min{cost(i,k) + cost(k,j)} for k:0-n-1`.** Repeat that question for all possible (i,j) then you have the Floy-Warshall algorithm.
- The dynamics: or the propagation direction of shortest path finding.
	+ In the initialization `k=0` only pairs `(i,j)` that have a direct connection (i.e. `e(i,j) ∈ E`, E is the edge set) have shortest path values or A<sub>i,j</sub>≠∞ where i≠j.
	+ In the next iteration where k = 1, we asked all nodes to check whether there is a shorter path via node with label 1 (or the first label) to all other nodes. Similarly at k-ith iterration we ask nodes to check the shortcuts via k-th node.
	+ At k = n, we ask all nodes to check shortcuts via the node with label n-th, and hence we already ask nodes to check shortcuts via all other nodes from k=1...n.
	+ Formula: A<sub>i,j,k</sub> = min {A<sub>i,j,k-1</sub>, A<sub>i,k,k-1</sub> + A<sub>k,j,k-1</sub>}
	+ Initial condition: A<sub>i,j,k=0</sub>:
		- `= 0` if `i == j`
		- = c<sub>ij</sub> if there is an edge (i,j)
		- `= ∞` otherwise
- To detect negative cost cycles, look for negative values on the diagonal A[i=j].

![Imgur](http://i.imgur.com/ELDafpM.png)

![Imgur](http://i.imgur.com/imkcz1B.png)

## Johnson's All Pair Shortest Path

Complexity: O(nmlogn), same as Dijkstra's algorithm for n pairs but with Bellman-Ford benefits: can be used with negative edge lengths and can detect negative cost cycles early in O(nm) time.

Idea: combine 2 algorithms and 1 technique
- Potential reweighting: the weights depend on start and end vertices only (potential). The technique hence can be used as a transform operation: from Dijkstra's problem to Bellmand-Ford's.
- Bellman-Ford's algorithm: to calculate the path-independent weights
- Dijkstra's algorithm: to actual find the shortest paths, invoked n times.

Algorithm:
- Create a new graph with all nodes grounded to a ground node, i.e. a new ground node that has one way connections to all the other nodes is created. This is analogous to bounding a potential function in physics or electricity. A clever way to eliminate the negative weights.
- Use Bellman-Ford to find single source shortest path from `ground` to all the other nodes. Call this `P(v)` where v the vertices. If negative cost cycles are detected we stop the algorithm here.
- Reweight all the edges as c'<sub>uv</sub> = c<sub>uv</sub> + P(u) - P(v) where c'<sub>uv</sub>  is the new weight of the edge (u,v) with u as the tail.
- Invoke n Dijkstra operations on the new reweighted graph where edge lengths now all become non-negative.
- Convert the shortest path values found back to the unweighted version c<sub>uv</sub> = c'<sub>uv</sub> - P(u) + P(v).

![Imgur](http://i.imgur.com/yNdyuMn.jpg)

## Kruskal's Algorithm for Minimum Spanning Tree Problem
Complexity: **O(mlogn)** using Union-Find data structure

![](http://algs4.cs.princeton.edu/43mst/images/kruskal.png)

Note: Asymptotically, O(mlogm) is equivalent to O(mlogn) since at most m = n<sup>2</sup> hence at most logm = 2logn and thus O(logm) = O(logn).

The idea: Sorting edges based on their costs. From the lowest to highest cost edges, keep adding the edge to the MST if it does not make a cycle when added. Pictorially, the algorithm forms multiple disconnected components (initially size n, meaning n disconnected components each contains a single vertex) and fuses them together when iterating over. The key point to the algorithm is in efficiently checking cyclic edges. To determine if an edge creates a cycle we need to be sure that it is not belong to the same component. The Union-Find datastructure makes it possible to efficiently check this property in constant time O(1) and O(logn) to maintain which all together contributes to O(mlogn) complexity. On the note of maintenance cost, there is a technique for updating leader nodes of the smaller size component, thus the size of the fused component keeps increasing of atleast 2 folds. Hence at most a logarithmic number of updates are needed to update the leader node.

![Imgur](http://i.imgur.com/Q7n1UxE.png)

Advanced:
- Theoreticall, it was proven (Pettie, Ramachandran, Chazelle) that the fastest algorithm possible for the MST problem is somewhere between linear and O(m) O(m α(n)) where α is the inverse Ackerman function, an extremely slow growing function, slower than log*n (log of log of log...).
- Randomized algorithm (Karger - Klein - Tarjan, 1995) can achieve O(m) efficiency. Of all the possible spanning trees find the one with the lowest cost.
- Union-Find datastructure. Lazy union. Path-compression technique. Union by rank (choose the smaller size component to update).

### Application: K-clustering

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4WCUFA5mGJADsiDn3HPxuuCQ6bXjVy32fDzGRJGXM0szwwnXj)

In machine learning, the k-clustering technique is used in unsupervised learning (without labels, compute similar groups based on defined similarity features). The execution of k-clustering method is similar to that of Kruskal's algorithm for MST, only that it might halt earlier (k, number of clusters, vs 1, which represents the single tree in MST). The algorithm keeps merging disconnected clusters, starting from maximum possible number of clusters (which is n) down to only k clusters, on the basis of eliminating pairs of points that has currently lowest similarity measures, such as Euclidean distances between points. Note that the number of clusters will reduce by one if the eliminated edge is the crossing edge.

Hamming distance: number of differences in corresponding i-th features of two sample points.

**Advanced problem** ([code here](k_cluster_big.py)): do the k-clustering on a dataset of 200000 points by Hamming distance measure to find maximum k at which min spacing is of a given value. There is a total of approx. 20 billions pairs to be considered (every point to every other points). Sorting O(mlogm) is almost impossible for m of this value. The trick is then to analyze the problem further. For small values of min-spacing (for 24 bits points, there is (24-1) points with 1 bit diffrence from a given point, 276 points with 2 bits difference. Hence, with a requirement of min-spacing not smaller than 3, there is a finite number of variations (23 + 276) we need to check and unite if necessary, which brings the complexity of O(n) for this approach. The constant values in complexity depend on the min-spacing requirement. For small min-spacing(s) and big dataset this solution is quite efficient compared to quadratic complexity of generic greedy methods O(mlogn) ([sample code here](k_cluster.py)).

**The takeaway here is even for seemingly over-complicated problems, careful analysis of boundary conditions or problem definition space, there might exist approaches that are able to exploit the boundary conditions and significantly reduce the hardness level.**

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

## Travelling Salesman Problem - NP-Hard - Dynamic Programming

![](http://i2.wp.com/www.rational-action.com/wp-content/uploads/2015/03/best-road-trip-major-landmarks-1024x548-1024x548.png?resize=625%2C334)

![](https://imgs.xkcd.com/comics/travelling_salesman_problem.png)

Problem: given a graph with n vertices, find a tour that visits each vertice exactly once and have minimum length.

Complexity: NP-hard for generic optimization instances, NP-complete for decision problems. O(n<sup>2</sup>2<sup>n</sup>) with Dynamic Programming for Euclidean graphs.

Algorithm: applying Dynamic Programming, following the same method in Bellman-Ford with additional constraints:
- Every path must visit exactly n nodes (the budget i is now fixed at n-1)
- The visited nodes are all distinct

Optimal substructure: if the first and last node to visit is i and j, respectively, then before j the path should come from one of the neighbor nodes k with minimum cost and has visited all nodes except j, that is:

L<sub>S,j</sub> = min(L<sub>S-{j},k</sub> + c<sub>kj</sub>) for k ∈ S-{j}, k terms to consider

where S is the set with all nodes and `S-{j}` the set with all nodes except j, L<sub>X,j</sub> is the shortest path visiting all nodes in X and ending at j.
Similarly, it would be that before k:

L<sub>S-{j},k</sub> = min(L<sub>S-{j,k},m</sub> + c<sub>mk</sub>) for m ∈ S-{j,k}, m terms to consider

Right before base case, there are n subproblems (q ∈ S):

L<sub>{i,q},q</sub> = c<sub>iq</sub>, 1 term to consider

At base case:

L<sub>{i},i</sub> = 0

So, in order to have L<sub>S,j</sub> we have to solve a factorial number of subproblems from n-1 down to 1. That is when Dynamic Programming comes to the rescue, at each level of subproblem of size s we donot need to solve the full spectrum thanks to the tabular lookup. There would be ∑(S) of possible subsets of size from 1 to n (think (n choose 1) + (n choose 2) + ... + (n choose n)) = 2<sup>n</sup>. For each set there is a O(n) choice of j (the end vertice) and O(n) amount of works (the min operation). That would be total of O(n<sup>2</sup> 2<sup>n</sup>).

[Code](salesman.py):

- Create a 2D array of A[S][j] where S holds the subset and j the endpoint in that subset.
- Init A<sub>S={0},0</sub> = 0 others ∞.
- For size m of the subset from 1 to n
	+ For all the possible sets with size m
		* For each possible endpoint j (in the current set of size m):
			+ Look at all possible point k prior to j and choose the min distance A[S-{j}][k] + d[k][j]:
				- `A[S-{j}][j] = min(A[S-{j,k}][k] + D[k][j])`

Practical results: the constant in O(n<sup>2</sup> 2<sup>n</sup>) appears to be 1.15 in this case (or might include the n<sup>2</sup> term)

| Number of nodes | Time (in minutes) |
| --------------- | ----------------- |
| 17              | 0.3               |
| 18              | 0.6               |
| 19              | 1.4               |
| 20              | 3.2               |
| 21              | 7.3               |
| 22              | 18.2              |
| ...             | ...               |
| 25              | 221.2 (inter't)   |

![Imgur](http://i.imgur.com/vImmTz2.png)

## Vertex Cover
Problem: given a graph G find a minimum set S of vertices such that for every edge (u,v) in G there is at least one vertex (either u or v) that is contained in S.

Complexity: O(n2<sup>k</sup>) where k is the size of the cover set (given k is small).

Theorem: if S, the vertex cover of a graph G, has size k then the size of the vertex cover of graph G<sub>u</sub> (with u deleted from G) would be k - 1.

Algorithm: piggy-backed on the theorem, starting at k (either given or guessed) we recursively on graph G:
- arbitrarily select an edge whose vertices are u and v and check if:
	1. whether G<sub>u</sub> has a vertex cover size of k - 1 by deleting u from G
 	1. or whether G<sub>v</sub> has a vertex cover size of k - 1 by deleting v from G
- if neither of the obove is correct than we conclude that the assumption of the size of the vertex cover being k was wrong and G can only has at most a vertex cover of size k - 1 (since if it is k then it must have a vertex cover size of k-1 if we delete a vertex u (or v) which was proven to be wrong)

## Knapsack Problem - NP-Hard - Dynamic Programming

Complexity: NP-Hard for optimization problems, NP-Complete for decision problems. Greedy heuristic O(n<sup>2</sup>v<sub>max</sub>)

## 2SAT Problem

Complexity: O(Strongly-connected-component) unlike the NP-complete of 3SAT problem.

Problem: check whether a set of m clauses C<sub>1</sub> ∩ C<sub>2</sub> ... C<sub>m</sub> where C<sub>i</sub> = (a<sub>j</sub> v a<sub>k</sub>) of n variables a<sub>1</sub>, a<sub>2</sub> ... a<sub>n</sub> is satisfiable, meaning there exists a set of boolean values a<sub>1</sub>, a<sub>2</sub> ... a<sub>n</sub> satisfies the m clauses.

Algorithm:
1. Papadimitriou randomized local search algorithm
	- Analysis by random walk
2. Convert clauses to implication graph and use Kosaraju's strongly connected component searching.
	- An x ∪ y clause translates to an edge from (-x, y) and (-y, x) in the implication graph.
	- The 2SAT instance is satisfiable if no x and -x pair is present in any strongly connected component in the implication graph.
	- The implication is that if there is a 2 way path from x to -x, it implies a contradiction since an assumed boolean value of x leads to a required boolean value -x, and that is unsatisfiable.
![](https://i.stack.imgur.com/5NuFl.png)
[Example](https://cs.stackexchange.com/questions/16311/drawing-an-implication-graph-for-2-sat-clauses?rq=1) where an unsatisfiable 2SAT instance translates to a graph with a single strongly connected component.
3. Back tracking

## Bulk Problems

This group of problems regards to problems solved in multiple paradigms (divide & conquer, dynamic programming, greedy) and by many techniques but in common can be reduced to a simple, often has known solution, problem. For example:

- SUM-2 problem for a wide range of target values instead of a single value
- Select k-th smallest items from an array, originated from the smallest item problem
- K-clustering by Hamming distance
- All pair shortest path (Floyd-Warshall).

Often we exploit the fact that they are all in the same set of data and hence the labor for a single problem might be reused to speedup others (shortest path). Or we can make use of the boundary conditions and narrow down the size of each single problem (SUM-2, k-clustering, k-th smallest).


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

## Probability and Statistics

Probability, in a nutshell, is more about prediction. In contrast, statistics is more into conclusion. It is important to know the difference, mainly due to the purpose that they are meant to serve, to better approach them. But it is equally important to understand the duo's organic relation. One (**probability**) is used to predict and the other (**statistics**) is to suggest what we should predict or correct what we predicted.

## Birthday Paradox

Given a group of 23 persons, there is a 50-50 chance that there is 2 persons having the same birthday. **A rule of thumb is that the 50-50 chance comes when we have the size of the population reaches squared root of the event universe `23 ~ sqrt(365)`**.

Another interesting fact is that if we relaxing the condition of exact same birthday to **within a week**, the chance comes significantly earlier at `sqrt(365/7) ~ 8`. It happens that only a group of 8 friends is very likely to celebrate a joint birthday party of 2 guys / gals.

# Bag-Of-Tricks Problems:

## Finding missing numbers

- Finding a missiung number in a unique and continous range with time O(n) and space O(1)
- Finding 2 missing numbers
- Finding 3
- Finding k in O(n) and O(k) space

[Reference](https://stackoverflow.com/q/3492302)

## Resources:

- CLRS - Cormen, Leiserson, Rivest, and Stein, Introduction to Algorithms (3rd edition)
- DPV - Dasgupta, Papadimitriou, and Vazirani, Algorithms
- KT - Kleinberg and Tardos, Algorithm Design
- SW  - Sedgewick and Wayne, Algorithms (4th edition)
