import xlsxwriter

wb = xlsxwriter.Workbook('sales_report.xlsx')

ws = wb.add_worksheet()

ws.write('A1', 'Person')
ws.write('B1', 'Sales')

data_str = ['Sales Person1', 'Sales Person2', 'Sales Person3', 'Sales Person4', 'Sales Person5']
data1 = [78000, 32000, 45000, 11000, 20000]

ws.write_column('A2', data_str)
ws.write_column('B2', data1)

c = wb.add_chart({'type': 'pie'})
c.add_series({
    'categories': ['Sheet1', 1, 0, 5, 0],
    'values': ['Sheet1', 1, 1, 5, 1]
})
c.set_title({'name': 'Sales_Report'})
ws.insert_chart('E4', c)
wb.close()
