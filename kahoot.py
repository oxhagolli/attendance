"""
    @author Orens Xhagolli
    This file will take the kahoot reports from both recitations during the week and combine them into one.
"""

import xlrd
import sys


def read_kahoot(filename):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(1)

    combined = []

    for rowx in range(3, sheet.nrows-2):
        cols = sheet.row_values(rowx)
        combined.append([cols[1], cols[3]])

    return combined


if len(sys.argv) != 4:
    print("Usage: python3 kahoot.py section1.xlsx section2.xlsx output.txt")
    exit(1)

result = read_kahoot(sys.argv[1]) + read_kahoot(sys.argv[2])

with open(sys.argv[3], "w+") as file:
    for element in result:
        file.write(element[0] + ", " + str(element[1]) + "\n")

print("Completed.")
