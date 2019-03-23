import openpyxl

file=openpyxl.load_workbook("/Users/arturbondarau/Desktop/NewClass/day10/Copy of Releases for QA coordination - September - December 2018 v0.1.QA.xlsx")
sheet=file["Sheet2"]

line_number=0
for row in sheet.iter_rows():
    line_number=line_number+1
    if line_number==1:
        continue
    line=[cell.value for cell in row]
    state={"state":line[0],"population":line[1]}
    print(state)