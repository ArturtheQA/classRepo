sample = [9,1,2,3,4,55,6,7,8,8,9,9,9,33,3,3,3,4,44,55,22]
search_criteria=9

position_of_the_value=-1

index=-1
while index<len(sample):
    
    value = sample[index]
    index=index+1
    if value==search_criteria:
        position_of_the_value=index
        print(position_of_the_value)