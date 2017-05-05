# Algorithms Divide and Conquer - Coursera
School: Coursera  
Class: Algorithms Divide and Conquer  
Lecturer: Tim Roughgarden - Professor at Stanford University  
Published: 2012  

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

Algorithm:
- Preprocessing: sort the data points in x to get Px, in y to get Py. Both contains the same data points, but in different orders.
- Divide: partition to left and right data points
	+ Take the index (n/2 where n is Px length) of the mid item in Px, get its x coordinate, name it x*, Px<sup>n+1</sup> will have the items from Px[0 ... n/2] on the left and Px[n/2+1 ... n] on the right
	+ Filter Py by x_bar: iterating from bottom to top in Py, if items have x coordinate less than x_bar, put it in Py<sup>n+1</sup><sub>left</sub>, otherwise in the right bucket Py<sup>n+1</sup><sub>right</sub>. By iterating from bottom to top, we preserve the y-increasing order. This is crucial!
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

## Resources:

- CLRS - Cormen, Leiserson, Rivest, and Stein, Introduction to Algorithms (3rd edition)
- DPV - Dasgupta, Papadimitriou, and Vazirani, Algorithms
- KT - Kleinberg and Tardos, Algorithm Design
- SW  - Sedgewick and Wayne, Algorithms (4th edition)
