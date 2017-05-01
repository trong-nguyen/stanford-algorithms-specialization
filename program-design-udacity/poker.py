# -----------
# User Instructions
# 
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands. 
# 
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens 
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function 
#                  returns their corresponding ranks as a 
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks 
#                  in a hand (where the order goes from
#                  highest to lowest rank). 
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will 
# tell you if you are correct.

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return ranks == range(ranks[0], ranks[0]-5, -1)

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for _,s in hand]
    return  suits == [suits[0]] * 5

def kind_naive(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    repetition = {}
    for r in ranks:
        repetition[r] = repetition.get(r, 0) + 1

    for rank, rep in repetition.items():
        if rep == n:
            return rank

    return None

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in set(ranks):
        if ranks.count(r) == n:
            return r

    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    tp = ()
    for r in set(ranks):
        if ranks.count(r) == 2:
            tp += (r,) # high will stay first, regardles, thanks to high sorted ranks

    if len(tp) == 2:
        return tp

    return None


def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    if key:
        transformed = list(zip(map(key, iterable), iterable))
        m, _ = max(transformed)
        return [j for i, j in transformed if i == m]
    else:
        m = max(iterable)
        return filter(lambda x: x == m, iterable)

def rank_to_int_naive(r):
    "Map higher than character ranks to intergers"
    m = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10
    }
    return m[r] if r in m else int(r)

def rank_to_int(r):
    return '--23456789TJQKA'.index(r)

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r,s in cards]
    ranks = map(rank_to_int, ranks)
    ranks.sort(reverse=True)
    return ranks if (ranks != [14, 5, 4, 3, 2]) else [5, 4, 3, 2, 1]

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    fl = "3H 6H TH AH 2H".split() # Flush
    st = "3H 4D 7D 6C 5C".split() # Straight
    sta = "3S 2H AS 4H 5D".split()# Straight with ace
    k3 = "9C 9D 9H 3D 6C".split() # 3 of a kind
    p2 = "8D 5C 8C 5H 3D".split() # 2 pairs
    k2 = "JD 3C 4H 8S JS".split() # 2 of a kind
    hc = "JS QS 4H 7C TH".split() # high card
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 7, 7, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False

    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert hand_rank(fl) == (5, [14, 10, 6, 3, 2])
    assert hand_rank(st) == (4, 7)
    assert hand_rank(k3) == (3, 9, [9, 9, 9, 6, 3])
    assert hand_rank(p2) == (2, (8, 5), [8, 8, 5, 5, 3])
    assert hand_rank(k2) == (1, 11, [11, 11, 8, 4, 3])
    assert hand_rank(hc) == (0, [12, 11, 10, 7, 4])
    # assert hand_rank(sta)== (4,)

    return 'tests pass'

test()