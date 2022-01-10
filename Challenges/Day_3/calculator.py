#Program of calculator to perform addition, substraction, multiplication and division using if & else.
num1=int(input("Enter number 1: "))
op=input("Enter the operation you want to perform: ")
num2=int(input("Enter number 2: "))

if op=='x' or op=='*':
    print(num1*num2)

elif op=='+':
    print(num1+num2)

elif op=='/':
    print(num1//num2)

elif op=='-':
    print(num1-num2)




