import csv

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
            if row[3] in ("column header", criterion):
                yield row
                count += 1
            if count > 5:
                return
        # return count

ff = getstuff("./Data/FeedGrains.csv", "Barley")
# print ff
print ff
for i in ff:
    print(i)
    print(i[15])
