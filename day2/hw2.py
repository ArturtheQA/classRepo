#hw2


#first solution
def day_checker_by_number():
    user_put_day=int(input("Please place day# and I will tell what day is it"))
    while user_put_day not in range(1,7):
        print("please put a day # from 1-7")
    else:
        if user_put_day == 1:
            print("Your day is Monday")
                   
        elif user_put_day==2:
            print("Your day is Tuesday")
                  
        elif user_put_day==3:
            print("Your day is Wednesday")
             
        elif user_put_day==4:
            print("Your day is Thursday")
              
        elif user_put_day==5:
            print("Your day is Friday")
            
        elif user_put_day==6:
            print("Your day is Saturday")
             
        elif user_put_day==7:
            print("Your day is Sunday")


#more officient way and less code
def day_checker_by_number1():
    weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    user_put_day=int(input("Please place day# and I will tell what day is it"))
    checker=user_put_day-1
    if checker in range(len(weekdays)):
        print(weekdays[checker])
        
    else:
        print("Please put number from 1 -7")
    

# day_checker_by_number()

day_checker_by_number1()