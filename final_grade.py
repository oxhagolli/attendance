from difflib import SequenceMatcher

import sys


def _best_match(relevant, keyword):
    ratio = sorted(relevant, key=lambda x: SequenceMatcher(None, x, keyword).ratio(), reverse=True)
    return ratio[0]


if len(sys.argv) != 3:
    print("Usage: python3 final_grade.py kahoot.txt present.txt")

kscore = {}
with open(sys.argv[1]) as kahoot:
    for line in kahoot:
        user, score = line.strip().strip(" ").split(",")
        kscore[user] = int(score)

present = {}
with open(sys.argv[2]) as pres:
    for line in pres:
        user, first, last = line.strip().strip(" ").split(", ")
        present[user] = 5

total = {}
for k, v in kscore.items():
    if k in present.keys():
        total[k] = v + 5
    else:
        total[k] = v

for k, v in present:
    if k not in total.keys():
        total[k] = 5

print(total)
