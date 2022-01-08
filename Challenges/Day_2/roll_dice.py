import random 
while True:
    a = random.randint(1,6)
    n = (input("Enter (y) to roll the dice else (n) to exit : "))
    if n=='y' or n=='Y':
        print("rolling the dice____wait__")
        print(a)
    elif n!='y':
        print("exit")
        break;
       
    
