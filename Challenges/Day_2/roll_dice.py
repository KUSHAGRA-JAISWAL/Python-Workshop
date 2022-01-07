import random 
roll = True
while roll:
    a = random.randint(1,6)
    print(a)
    n = int(input("Enter 1 to roll again else 2 to exit : "))
    if n==2:
        roll = False

    