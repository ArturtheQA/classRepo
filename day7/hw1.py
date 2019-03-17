import random
values=[9,1,2,3,4,55,6,-7,8,8,9,9,-9,33,-3,3,3,4,44,55,-22]
streets=["first","second","third"]
towns=["brooklyn","nyc"]
states=["ny","nj","oh"]
zips=["11234","11223","11215"]
# #need to do
# def minimum(values):
#     for i in values:
#     lambda i,y: x if x<y else y, values

#     print(a)

# minimum(values)

# def fibonachi(input1,maxinput):
#     input1=int(input("Where to start"))
#     maxinput=int(input("Where to finish"))

#     while input1<maxinput:
#          input2=input1+1
#          print(input1+input2)




def termitanor():
    a=["i will be back","Hasta la vista", "Smile"]
    print(a[random.randrange(0,len(a))])

termitanor()

def adress_Verify():
    street=input('Please palace some street')
    town = input('please place some town')
    state=input('please place some state')
    zip=input('please place some zip')
    if street in streets and town in towns and state in states and zip in zips:
        print("adress is correct")


adress_Verify()

def street_validation(street,town,state,zip):
        is_street_valid = street is not None and len(str(street).strip())
        if not is_street_valid:
            return False
        return True



 