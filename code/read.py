import csv
import sys
from sets import Set
# Using these 2 to effectively read the large data file
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
# https://stackoverflow.com/questions/7883962/where-to-use-yield-in-python-best

def getstuff(filename, criterion):
    with open(filename, "rb") as csvfile:
        datareader = csv.reader(csvfile)
        count = 0
        m = 0
        for row in datareader:
            m += 1
            # count += 1
            # print row[3]
            # yield row
            # if m > 1000:
            if row[3] in ("column header", criterion) and len(row[17]) == 3:
                yield row
                count += 1
                print row
                sys.exit(0)
            # if count > 5:
            #     return
        # return count

ff = getstuff("./Data/FeedGrains.csv", "Barley")
# print ff
# print ff
months = Set()

for i in ff:
    # print(i)
    months.add(i[17])
    # print(i[17])



for m in months:
    print m
