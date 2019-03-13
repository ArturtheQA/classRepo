#day 2 hw1





def leap_year_checker(input):

    if ((input%4)==0 and (input %400!=0)) :
        print("It seems like year ",user_enter_year," in a leap year")
    else:
        print("I think year", user_enter_year," is not a leap year")
        
user_enter_year=int(input("Please enter a year and programm will calculate is it a leap year or not"))
leap_year_checker(user_enter_year)
