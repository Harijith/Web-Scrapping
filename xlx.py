import xlsxwriter
workbook=xlsxwriter.Workbook("e://myscheet.xlsx")
worksheet=workbook.add_worksheet()
worksheet.write("A1","Name")
worksheet.write("B1","Marks")
chart=workbook.add_chart({'type':'bar'})
chart.add_series({'values':'=Sheet1!$B$1:$C$30'})
worksheet.insert_chart('D1',chart)
workbook.close()

