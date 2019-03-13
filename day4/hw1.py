#  print all even numbers of the given array
# - print all negative numbers of the given array
# - print indices of all odd numbers of the given array
# - print sum of all values at odd indices of the given array
# - print sum of all odd values of the given array
# - count odd numbers in the given array
# - find average value of the even numbers in the given array
# - find difference between (a - b) odd values and even values of the given array

value=[-1,2,3,4,5,6,7,8,9]
def even_number_checker(value):
    
    for i in range(len(value)):
        if i%2==0 and i>0:
            print(i)


#even_number_checker(value)
# - print all negative numbers of the given array
def negative_number_checker(value):
    
    for i in (value):
        if i<0:
            print(i)

# negative_number_checker(value)

# - print indices of all odd numbers of the given array

def odd_number_index(value):
    
    for i in range(len(value)):
        if i%2==1 and i>0:
            print(i*i)

# odd_number_index(value)
# - print sum of all odd values of the given array
def odd_number_summary(value):
    
    for i in range(len(value)):
        summary=0
        if i%2==1 and i>0:
            summary=summary+i
            print(summary)
            
# odd_number_summary(value)
# - count odd numbers in the given array
def odd_number_counter(value):
    
    for i in range(value):
        counter=0
        if i%2==1 and i>0:
            counter=counter+1
            print(counter)
# odd_number_counter(value)
# - find average value of the even numbers in the given array
def number_average(value):
    sum=0
    for i in value:
        sum=sum+i
    print (sum/len(value))

       
# number_average(value)

def min_and_max(value):
    minimum=0
    maximum=0
    for i in value:
        if i<minimum:
            minimum=i
        else :
            if i>maximum:
                maximum=i
    print(maximum)
    print(minimum)
    print(maximum/minimum)
# min_and_max(value)

def prime_number():
    is_prime=False
