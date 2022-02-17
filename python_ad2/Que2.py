import xlsxwriter

wb = xlsxwriter.Workbook('student_report.xlsx')

ws = wb.add_worksheet()

ws.write('A1', 'Student')
ws.write('B1', 'Maths')
ws.write('C1', 'Science')
ws.write('D1', 'English')

std_marks_maths = {
    'Zecil': 91,
    'Pranshu': 87,
    'Neil': 81
}
std_marks_science = {
    'Zecil': 89,
    'Pranshu': 91,
    'Neil': 87
}
std_marks_english = {
    'Zecil': 95,
    'Pranshu': 94,
    'Neil': 92
}
row = 1
row1 = 1
row2 = 1

for std, marks in std_marks_maths.items():
    ws.write(row, 0, std)
    ws.write(row, 1, marks)
    row += 1

for marks in std_marks_science.values():
    ws.write(row1, 2, marks)
    row1 += 1

for marks in std_marks_english.values():
    ws.write(row2, 3, marks)
    row2 += 1

c1 = wb.add_chart({'type': 'line'})
c1.add_series({
    'categories': ['Sheet1', 0, 1, 0, 3],
    'values': ['Sheet1', 1, 1, 1, 3]
})
c2 = wb.add_chart({'type': 'line'})
c2.add_series({
    'categories': ['Sheet1', 0, 1, 0, 3],
    'values': ['Sheet1', 2, 1, 2, 3]
})
c3 = wb.add_chart({'type': 'line'})
c3.add_series({
    'categories': ['Sheet1', 0, 1, 0, 3],
    'values': ['Sheet1', 3, 1, 3, 3]
})
ws.insert_chart('E1', c1)
ws.insert_chart('K2', c2)
ws.insert_chart('Q3', c3)
wb.close()
