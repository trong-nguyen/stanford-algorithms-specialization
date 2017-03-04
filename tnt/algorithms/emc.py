import random
hyp = math.hypot

# Courtesy of and forked from https://www.nayuki.io/page/smallest-enclosing-circle
# 
# Data conventions: A point is a pair of floats (x, y). A circle is a triple of floats (center x, center y, radius).

# 
# Returns the smallest circle that encloses all the given points. Runs in expected O(n) time, randomized.
# Input: A sequence of pairs of floats or ints, e.g. [(0,5), (3.1,-2.7)].
# Output: A triple of floats representing a circle.
# Note: If 0 points are given, None is returned. If 1 point is given, a circle of radius 0 is returned.
# 
# 
# 
_E = 1e-12

def _is_in_circle(c, p):
    return c is not None and hyp(p[0] - c[0], p[1] - c[1]) < c[2] + _E

def _is_on_circle(c, p, r):
    return abs( hyp(p[0] - c[0], p[1] - c[1])**2 - r ) <  _E

def make_circle(ps):
    # Convert to float and randomize order
    s = [ map(float, p) for p in ps ]
    random.shuffle(s)
    
    # Progressively add points to circle or recompute circle
    c = None
    for (i, p) in enumerate(s):
        if c is None or not _is_in_circle(c, p):
            c = _circle_one_point(s[0 : i + 1], p)
    return c

def smallestCircle(ps):
    a = make_circle(ps)[-1]
    lu = [ map(int, i) for i in a ]
    if len(a) == 2:
        u,v = a
        r = ( (u[0]-v[0])**2 + (u[1]-v[1])**2 ) / 4.
        c = [ .5*(u[0]+v[0]), .5*(u[1]+v[1]) ]
        for p in ps:
            if p not in lu:
                if _is_on_circle(c, p, r):
                    lu += [p]
                
    r = sorted([ ps.index(i) for i in lu ])
    return r

# One boundary point known
def _circle_one_point(ps, p):
    c = (p[0], p[1], 0.0)
    for (i, q) in enumerate(ps):
        if not _is_in_circle(c, q):
            if c[2] == 0.0:
                c = _diameter(p, q)
            else:
                c = _circle_two_points(ps[0 : i + 1], p, q)
    return c


# Two boundary points known
def _circle_two_points(ps, p, q):
    diameter = _diameter(p, q)
    if all(_is_in_circle(diameter, r) for r in ps):
        return diameter
    
    left = None
    right = None
    for r in ps:
        cross = cxs(p[0], p[1], q[0], q[1], r[0], r[1])
        c = _circumcircle(p, q, r)
        if c is None:
            continue
        elif cross > 0.0 and (left is None or cxs(p[0], p[1], q[0], q[1], c[0], c[1]) > cxs(p[0], p[1], q[0], q[1], left[0], left[1])):
            left = c
        elif cross < 0.0 and (right is None or cxs(p[0], p[1], q[0], q[1], c[0], c[1]) < cxs(p[0], p[1], q[0], q[1], right[0], right[1])):
            right = c
    return left if (right is None or (left is not None and left[2] <= right[2])) else right



def _circumcircle(p0, p1, p2):
    # Mathematical algorithm from Wikipedia: Circumscribed circle
    ax, ay = p0
    bx, by = p1
    cx, cy = p2
    d = (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) * 2.0
    if d == 0.0:
        return None
    x = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    y = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return (x, y, hyp(x - ax, y - ay), [p0, p1, p2])


def _diameter(p0, p1):
    return ((p0[0] + p1[0]) / 2.0, (p0[1] + p1[1]) / 2.0, hyp(p0[0] - p1[0], p0[1] - p1[1]) / 2.0, [p0,p1])






# Returns twice the signed area of the triangle defined by (x0, y0), (x1, y1), (x2, y2)
def cxs(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)