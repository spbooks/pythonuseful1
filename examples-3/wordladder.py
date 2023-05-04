#!/usr/bin/env python3

import sys
import copy
import unittest

# read the list of words into a set
with open("/usr/share/dict/words") as fp:
    words = set([x.strip() for x in fp.readlines()
                    if len(x.strip()) == 4 and x == x.lower()])


# Test whether our functions do what we expect
class TestFunctions(unittest.TestCase):
    def test_change(self):
        self.assertEqual(
            change("abcd", 0, set(["abcd", "bbcd", "cbcd", "aaaa"])),
            set(["bbcd", "cbcd"])
        )
        self.assertEqual(
            change("abcd", 1, set(["abcd", "bbcd", "cbcd", "aaaa"])),
            set([])
        )
        self.assertEqual(
            change("abcd", 2, set(["abcd", "bbcd", "cbcd", "aaaa"])),
            set([])
        )

    def test_step(self):
        queue = ["abcd"]
        chain = {"abcd": []}
        used = set(["abcd"])
        words = set(["abcd", "bbcd", "aaaa"])
        step(queue, chain, used, words)
        self.assertEqual(queue, [])
        self.assertEqual(used, set(["abcd", "bbcd"]))
        self.assertEqual(chain, {"abcd": [], "bbcd": ["abcd"]})


def change(word, charidx, words):
    matches = copy.copy(words)
    for i in range(len(word)):
        if i == charidx:
            matches = [x for x in matches if x[i] != word[i]]
        else:
            matches = [x for x in matches if x[i] == word[i]]
    return set(matches)


def step(queue, chain, used, words):
    nxt = queue.pop(0)
    changes = (list(change(nxt, 0, words)) + list(change(nxt, 1, words)) +
               list(change(nxt, 2, words)) + list(change(nxt, 3, words)))
    changes = [c for c in changes if c not in used]
    for c in changes:
        chain[c] = chain[nxt] + [nxt]
        used.add(c)
        queue.append(c)


def win(wto, wfrom, chainfrom, chainto):
    matches = wto.intersection(wfrom)
    if matches:
        m = list(matches)[0]
        return chainfrom[m] + [m] + list(reversed(chainto[m]))


# Find a ladder which begins with w1 and ends with w2
def ladder(w1, w2):
    # throw an error if one of the words is unknown
    for w in [w1, w2]:
        if w not in words:
            raise Exception(f"Unknown word {w}")

    # two sets of words that we have reached, starting from the from and to words
    wfrom = set()
    wto = set()
    # a queue, showing what we've checked for each word
    qfrom = [w1]
    qto = [w2]
    # the steps taken to get to each word
    chainfrom = {w1: []}
    chainto = {w2: []}

    while True:
        try:
            # "evolve" the from words one more step by finding all possible
            # new words from each word already in the list
            step(qfrom, chainfrom, wfrom, words)
            # compare the list of evolved from words with the list of evolved
            # to words to see if there's any overlap
            res = win(wto, wfrom, chainfrom, chainto)
            # if there is an overlap, then we have found a ladder! return it
            if res: return res
            # evolve the to words
            step(qto, chainto, wto, words)
            # and check again
            res = win(wto, wfrom, chainfrom, chainto)
            if res: return res
        except IndexError:
            return ["No ladder found"]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Syntax: {sys.argv[0]} word word")
        sys.exit(1)
    w1, w2 = sys.argv[1].lower(), sys.argv[2].lower()
    if len(w1) != 4 or len(w2) != 4:
        print(f"Syntax: {sys.argv[0]} word word")
        sys.exit(1)
    if w1 == "test" and w2 == "test":
        unittest.main(argv=[sys.argv[0]])
    else:
        res = ladder(w1, w2)
        print("\n".join(res))
        if type(res) == list:
            print(f"{len(res)} steps")