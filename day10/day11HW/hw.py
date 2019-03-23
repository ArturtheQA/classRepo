# 1.A local warehouse needs to create a delivery tracking system. 
# When customers order goods, they provide shipping addresses.
#  Your task is testing/verifying addresses (use the function we created in previous classes)
#   and print their validation result on the screen. Addresses are stored in an Excel file (I will provide the file after the class).
# 2Now write the testing results into an Excel file (instead of printing).
# 3Now implement functionality for reading the Excel file from previous task.
# 4Bonus: good design of classes and a new package for the solution
import csv

a=list(open("/Users/arturbondarau/Desktop/NewClass/day10/day11HW/adress.csv","r"))     
b=list(open("/Users/arturbondarau/Desktop/NewClass/day10/day11HW/Brooklyn_zip.csv","r"))


def validation_adresss_ny(streets, zipcode):
    print(a,b)
    if streets in a and zipcode in b:
        print("Your address is correct")
    else:
        print("It is not correct address, you loser")
    
validation_adresss_ny("eight",11215)