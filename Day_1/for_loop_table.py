#Program to show to concept of for loop and to print the tables of given numbers.
a = int(input("Enter a first number for Table: "))
b = int(input("Enter a second number for Table: "))
for count in range(1,11):
   
    print(a*count, end=" ")
    print(b*count)
