x = 10
y = 55
z = 0


# if x> y:
#     min=y
# if x ==y:
#     min =x 

# if min <z:
#     min =z
# if min >z:
#     min=min
# if min==z:
#     min=min
# print(min)



# if x>y:
#     example=y
# if y > z:
#     example=z
# print(x)

# print("min is",max(x,y,z))




def comp_algo_min(arg1,arg2,arg3):
    if (arg1 - arg2)>0:
        if (arg2 - arg3)>0:
            print(arg3)
    elif (arg3-arg2)>0:
        if (arg2-arg1)>0:
            print(arg1)
    elif (arg2-arg3)>0:
        if (arg3-arg1)>0:
            print(arg1)

comp_algo_min(x,y,z)