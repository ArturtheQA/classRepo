# makes={"makes1":["car1","car2","car3"],"makes2":["car4","car5"]}
# print(makes["makes1"])=l


def countdown(n):
    if n == 0:
        print (0)
    else:
        print (n)
        countdown(n-1)

countdown(5)