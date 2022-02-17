import xlsxwriter

wb = xlsxwriter.Workbook('Olympics.xlsx')

ws = wb.add_worksheet()

# cat_str = ['Country', 'Gold', 'Silver', 'Bronze', 'Total']
ws.write('A1', 'Country')
ws.write('B1', 'Gold')
ws.write('C1', 'Silver')
ws.write('D1', 'Bronze')
ws.write('E1', 'Total')

data1 = ['Country1', 'Country2', 'Country3', 'Country4', 'Country5']
data2 = [15, 8, 12, 21, 18]
data3 = [20, 15, 25, 12, 29]
data4 = [25, 10, 10, 13, 30]
data5 = [60, 33, 47, 50, 77]
ws.write_column('A2', data1)
ws.write_column('B2', data2)
ws.write_column('C2', data3)
ws.write_column('D2', data4)
ws.write_column('E2', data5)

c = wb.add_chart({'type': 'column'})
c.add_series({
    'name': ['Sheet1', 0, 1],
    'categories': ['Sheet1', 1, 0, 5, 0],
    'values': ['Sheet1', 1, 1, 5, 1]
})
c.add_series({
    'name': ['Sheet1', 0, 2],
    'categories': ['Sheet1', 1, 0, 5, 0],
    'values': ['Sheet1', 1, 2, 5, 2]
})
c.add_series({
    'name': ['Sheet1', 0, 3],
    'categories': ['Sheet1', 1, 0, 5, 0],
    'values': ['Sheet1', 1, 3, 5, 3]
})
c1 = wb.add_chart({'type': 'line'})
c1.add_series({
    'name': ['Sheet1', 0, 4],
    'categories': ['Sheet1', 1, 0, 5, 0],
    'values': ['Sheet1', 1, 4, 5, 4]
})
c.set_title({'name': 'Medal Tally'})
ws.insert_chart('A8', c)
c1.set_title({'name': 'Total_Tally'})
ws.insert_chart('I8', c1)
wb.close()
