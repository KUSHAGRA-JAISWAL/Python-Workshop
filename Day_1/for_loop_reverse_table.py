#Program to show to concept of for loop and to print the tables of given numbers in Revers form.
a = int(input("Enter a first number for Table: "))
b = int(input("Enter a second number for Table: "))
for count in range(10,0,-1):
   
    print(a*count, end=" ")
    print(b*count)
