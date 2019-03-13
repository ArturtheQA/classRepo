# hw3
import random
# degining of the programm
a = 0
b = 0


def number_selector():
    # global a
    # global b
    a = random.randint(1, 10)

    b = random.randint(1, 10)

    print("Hi there! I want ot play a game with you. I will show you 2 numbers and you have to calculate them! Your numbers are:")
    print(a)
    print(b)
    return (a, b)


def multiplier_check(a, b):
    user_input_multiplier = int(input("What will be the result?"))
    if user_input_multiplier != a*b:
        print("you loose")
    else:
        print("ypu won!")


(a, b) = number_selector()
print(a,b)
multiplier_check(a, b)
