# def min(somevalue):
#     value=max(somevalue)
#     for value1 in somevalue:
#         if value1<value:
#             value=value1
#     print(value)
#     return value
# array=[1,2,3,4,5,6,7,89,-11,-22]



def max(somevalue):
    value=min(somevalue)
    for value1 in somevalue:
        if value1>value:
            value=value1
    print(value)
    return value

array=[1,2,3,4,5,6,7,89,-11,-22]

max(array)