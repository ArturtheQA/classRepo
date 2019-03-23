import openpyxl

file= openpyxl.load_workbook("/Users/arturbondarau/Desktop/NewClass/day10/Copy of Releases for QA coordination - September - December 2018 v0.1.QA.xlsx")
sheet=file["Sheet2"]
sheet["A1"]="lol"
sheet["B1"]="ololol"
file.save

for row in sheet.iter_rows():
    line = [cell.value for cell in row]

    print(line)