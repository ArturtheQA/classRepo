line=[10,-3,5,100,-7]

def find_min(line,index,min):
    if index >=len(line):
        return min
    min=min if min < line[index] else line[index]
    return find_min(line,index+1,min)
print(find_min(line,0,line[0]))

def find_max(somevalue,index,maxvalue):
    if index>=len(somevalue):
        return maxvalue

    maxvalue=maxvalue if maxvalue > somevalue[index] else somevalue[index]
    return find_max(somevalue,index+1,maxvalue)

print(find_max(line,0,line[0]))