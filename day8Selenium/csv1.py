import csv


with open("/Users/arturbondarau/Desktop/NewClass/day8Selenium/selenium_test1.csv") as csv_file:
    reader = csv.reader(csv_file)
    
    for row in reader:
        for cell in row:
            print(cell)