"""
From the GCHQ Christmas 2022 puzzle challenge
https://www.gchq.gov.uk/news/xmaschallenge2022

F (yellow) O (blue) R (white)
M (blue) A (green) T (gold)
I (blue) O (gold) N (green)

1. Replace all the blue cells with a letter from PART
2. Replace all the green cells with a letter from EYES
3. Replace all the gold cells with a letter from UNCURL
After each step you should have three 3-letter words
in the rows of the grid, and you need to finish with a
9-letter word in the same formation as FORMATION.
"""

def get_replacements(word, to_replace, replace_with):
    replacements = [word[:to_replace] + x + word[to_replace+1:] for x in replace_with]
    replacements = [w for w in replacements if w in words3 and w != word]
    return replacements

# read the list of words into a set
with open("/usr/share/dict/words") as fp:
    words3 = set([x.strip() for x in fp.readlines()
                    if len(x.strip()) == 3 and x == x.lower()])
    words9 = set([x.strip() for x in fp.readlines()
                    if len(x.strip()) == 9 and x == x.lower()])

blueletters = "part"
greenletters = "eyes"
goldletters = "uncurl"

# Step 1: replace all the blue cells with a letter from "part"
word1_step1_possibilities = get_replacements("for", to_replace=1, replace_with=set("part"))
word2_step1_possibilities = get_replacements("mat", to_replace=0, replace_with=set("part"))
word3_step1_possibilities = get_replacements("ion", to_replace=0, replace_with=set("part"))

print("After replacing blue letters")
print("Word 1 could be any of", word1_step1_possibilities)
print("Word 2 could be any of", word2_step1_possibilities)
print("Word 3 could be any of", word3_step1_possibilities)

# Step 2: replace all the green cells with a letter from "eyes"
word1_step2_possibilities = word1_step1_possibilities # no green cells!

word2_step2_possibilities = []
for w in word2_step1_possibilities:
    word2_step2_possibilities += get_replacements(w, to_replace=1, replace_with=set("eyes"))

word3_step2_possibilities = []
for w in word3_step1_possibilities:
    word3_step2_possibilities += get_replacements(w, to_replace=2, replace_with=set("eyes"))

print("After replacing green letters")
print("Word 1 could be any of", word1_step2_possibilities)
print("Word 2 could be any of", word2_step2_possibilities)
print("Word 3 could be any of", word3_step2_possibilities)

# Step 3: replace all the gold cells with a letter from "uncurl"
word1_step3_possibilities = []
for w in word1_step2_possibilities:
    word1_step3_possibilities += get_replacements(w, to_replace=0, replace_with=set("uncurl"))

word2_step3_possibilities = []
for w in word2_step2_possibilities:
    word2_step3_possibilities += get_replacements(w, to_replace=2, replace_with=set("uncurl"))

word3_step3_possibilities = []
for w in word3_step2_possibilities:
    word3_step3_possibilities += get_replacements(w, to_replace=1, replace_with=set("uncurl"))

print("After replacing gold letters")
print("Word 1 could be any of", word1_step3_possibilities)
print("Word 2 could be any of", word2_step3_possibilities)
print("Word 3 could be any of", word3_step3_possibilities)

# Step 4: find the combination that is a 9-letter word
for w1 in word1_step3_possibilities:
    for w2 in word2_step3_possibilities:
        for w3 in word3_step3_possibilities:
            print("Possible nine-letter word:", w1+w2+w3)
