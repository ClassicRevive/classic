#!/usr/bin/env python

''' calculate probability of each rank of hand occuring given all hands'''

import sys

# define dictionaries of rank names and rank counters

ranknames = {"rank0": "nothing",
             "rank1": "one pair",
             "rank2": "two pairs",
             "rank3": "three of a kind",
             "rank4": "a straight",
             "rank5": "a flush",
             "rank6": "a full house",
             "rank7": "four of a kind",
             "rank8": "a straight flush",
             "rank9": "a royal flush"}
ranks = {}

def generate_hands():
    pass

def probability(s):
    probability = (ranks[s] / hands) * 100
    return probability


def main():
    global hands
    hands = 0

    for hand in sys.stdin:
        rank_num = str(hand.split(",")[-1].strip())
        rank = "rank" + rank_num

        if rank not in ranks:
            ranks[rank] = 0
        ranks[rank] += 1

        hands += 1

    for score in sorted(ranks):
        rank_name = ranknames[score]
        print ("The probability of {} is {:.4f}%".format(rank_name, probability(score)))


if __name__ == '__main__':
    main()
