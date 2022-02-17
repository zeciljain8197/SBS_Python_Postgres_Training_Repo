import csv

f1 = open('CSV_DATA.csv')

csv_r = csv.reader(f1)

lst = []
for line in csv_r:
    lst.append(tuple(line))

lst1 = sorted(lst, key=lambda x: x[1])
for i in range(0, len(lst1)-1):
    print(lst1[i])

f1.close()
