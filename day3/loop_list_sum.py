nums=[10,5,1]
#summary
sum=0
multy=1
for num in nums:
    sum=sum+num
    print(sum)

#multy number
for num in nums:
    multy=num*multy
    print(multy)
#len

print(len(nums))

counter=0
for num in nums:
    counter=counter+1
print(counter) 
#min number
min= nums[0]
for num in nums:
    if num < min:
        min=num
print(min)
#max number from the list
max=nums[0]
for num in nums:
    if num>max:
        max=num
print(max)