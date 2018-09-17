from difflib import SequenceMatcher

import random
import sys


def read_classlist(filename):
    relevant = []
    with open(filename) as file:
        for line in file:
            relevant.append(line.strip().strip("#").split(",")[:3])
    return relevant[1:]


def take_attendance(relevant, write="present.txt"):
    # flatten relevant
    rel = [x[0] + " " + x[2] + " " + x[1] for x in relevant]
    data = {x[0]: x[1] + ", " + x[2] for x in relevant}

    # Check if we want to take attendance
    ans = input("Would you like to take attendance? (y/n): ")
    if ans != 'y':
        return relevant  # Assumes everyone is present
    present = {}
    while len(rel) > 0:
        att = input("Next student: ")
        if att == 'stop':
            break
        print("Finding best match ...")
        student = _best_match(rel, att)
        check = input("Is this okay? (y/n) - " + student + ":")
        if check != 'y':
            continue
        else:
            username = student.split(" ")[0]
            rel.remove(student)
            present[username] = data[username]
    if write is not None:
        with open(write, "w+") as file:
            for k, v in present.items():
                file.write(k + ", " + v + "\n")
    return present


def _best_match(relevant, keyword):
    ratio = sorted(relevant, key=lambda x: SequenceMatcher(None, x, keyword).ratio(), reverse=True)
    return ratio[0]


def pair_students(pres, write="pairs.txt"):
    users = list(pres.keys())
    random.shuffle(users)
    pairs = []
    while len(users) >= 2:
        pairs.append([users[0], users[1]])
        del users[0]
        del users[0]
    if len(users) != 0:
        pairs[-1].append(users[0])
    expand_pairs = []
    for i in pairs:
        expand_pairs.append([pres[x] for x in i])
    if write is not None:
        with open(write, "w+") as file:
            for pair in expand_pairs:
                file.write(" - ".join(pair) + "\n")
    return expand_pairs


if len(sys.argv) < 2:
    print("Usage: python3 attendance.py classlist_from_mycourses.csv")
    exit(1)
relevant = read_classlist(sys.argv[1])
present = take_attendance(relevant)
pairs = pair_students(present)
for pair in pairs:
    print(" - ".join(pair))
