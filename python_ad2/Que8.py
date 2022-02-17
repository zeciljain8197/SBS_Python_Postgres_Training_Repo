import csv

headers = ['Name', 'Location', 'Strength']

values = [
    ['Infosys','Pune',40000],
    ['TCS','Gandhinagar',80000],
    ['Wipro','Banguluru',65000],
    ['Accenture','Gurugram',45000],
    ['Capegemini','Mumbai',32000],
]

f1 = open('Company_Details.csv', 'w')

csv_w = csv.writer(f1)

csv_w.writerow(headers)
csv_w.writerows(values)

f1.close()