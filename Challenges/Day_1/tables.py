#Program to print all the tables as per the requirement of the user.
a = int(input("Enter a starting point for Table: "))
b = int(input("Enter a end point for Table: "))

for i in range(1,11):
    for j in range(a,b+1):
      #  print(i*j,end="-")
      print(f"{j} X {i} = {j*i}",end="    ")
     

    print(" ")
    
