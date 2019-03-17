#File represents testing File with Artur's practice 
#####
# Comonn modules and vlues
values=[1,2,3,5,6,7,8,9,-1,-22,34,-400,1231,-2]


# Implement min() for numbers
# Implement max() for numbers
# Implement factorial(n)
# Print even numbers from the list using filter()
# A function that finds if the given list contains duplicate values 
# Print a sequence of Fibonacci numbers: 1, 1, 2, 3, 5, 8, …
# Flood-fill algorithm – paint the inside of the given closed area
# #####

# Implement min() for numbers
def minimum(values):
    y=0
    minimumvalue=0
    for i in values:
        minimumvalue=lambda i,y: y if i >y else i,values
    print(minimumvalue)
    


def factorial(number):
    #This class will do factorial for a number for example factorial of 3 = 3*2*1=6, 4 = 4*3*2*1=22
    number=number*number/number
    
    factorialsummary=1
    calculation=0
    while number!=0:
        lesser_argument=number-1
        calculation=number*lesser_argument
        factorialsummary=factorialsummary*calculation
        number=number-1
    print(factorialsummary)

factorial(3)