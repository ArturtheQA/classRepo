def factorial(number=input("place a number")):
    minus=0
    miltipler=number-minus
    while minus!=number:
        factorial=number*miltipler
        minus=minus+1
    print(factorial)


def factorial_1(n):
    if n<1:
        return 1

    return n* factorial(n-1)

