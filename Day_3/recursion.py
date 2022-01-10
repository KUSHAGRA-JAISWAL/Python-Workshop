#Program to show the concept of recursion and to calculate the factorial of the given number.
n=int(input("Enter a number: "))
def calc(n):
                if n==1:
                                return 1
                return n*calc(n-1)
print(calc(n))
