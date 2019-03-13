sample = [1,2,3,4,5,6,-1,7,8,9,-6]


def all_negative_numbers(some_values_here):
    index=0
    while index < len(some_values_here):
        for i in some_values_here:
            if i < 0:
                print(i)
            i=i+1
    index=index+1

all_negative_numbers(sample)