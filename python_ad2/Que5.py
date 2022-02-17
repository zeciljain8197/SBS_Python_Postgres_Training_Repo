import xlrd

file = xlrd.open_workbook('Employees.xlsx')
sheet = file.sheets()

for sheet in sheet:
    pass
male = []
female = []
for index in range(sheet.nrows):
    k = sheet.row_values(index, 0, sheet.ncols)
    if k[2] == 'Male':
        male.append(k)
    elif k[2] == 'Female':
        female.append(k)
    else:
        male.append(k)
        female.append(k)

list1 = []
k = 0
for i in range(0, 5):
    k += 1
    a1 = dict(zip(male[0], male[k]))
    list1.append(a1)

k = 0
list2 = []
for i in range(0, 6):
    k += 1
    a1 = dict(zip(female[0], female[k]))
    list2.append(a1)

demo_list = ['Male', 'Female']
demo_list1 = [list1, list2]
print(dict(zip(demo_list, demo_list1)))
