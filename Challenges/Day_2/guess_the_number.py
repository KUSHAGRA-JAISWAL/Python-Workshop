import random 
roll = True

a = random.randint(1,6)
while roll:
   # print(a)
    n = int(input("Make a guess between 1 to 6 : "))
    
    if a>n:
        print("too low")

    elif a<n:
        print("too high")

    else:
        roll=False
        print("correct")

        
