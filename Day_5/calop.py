''' additon
    substraction
    multiplication
    division
    exponent
    factorial
    log
    exp(e)
    summesion
    square
    sqrt
    cube'''
import math
def add():
    num1=float(input("Enter number 1: "))
    num2=float(input("Enter number 2: "))
    sum_=num1+num2
    print(f"sum of {num1} and {num2} is {sum_}")


def subs():
    num1=float(input("Enter number 1: "))
    num2=float(input("Enter number 2: "))
    sub=num1-num2
    print(f"substraction of {num1} and {num2} is {sub}")

def multy():
    num1=float(input("Enter number 1: "))
    num2=float(input("Enter number 2: "))
    mul=num1*num2
    print(f"Multiplication of {num1} and {num2} is {mul}")

def div():
    num1=float(input("Enter number 1: "))
    num2=float(input("Enter number 2: "))
    dive=num1/num2
    print(f"Division of {num1} and {num2} is {div}")

def mysqrt():
    num1=float(input("Enter number : "))
    res=math.sqrt(num1)
    print(f"squareroot of {num1} is {res}")
    
def facto():
    num1=int(input("Enter number : "))
    f=math.factorial(num1)
    print(f"squareroot of {num1} is {f}")

def pow():
    num1=float(input("Enter number 1: "))
    num2=float(input("Enter number 2: "))
    pow_=num1**num2
    print(f"power of {num1} and {num2} is {pow_}")
   
def srq():
    num1=float(input("Enter number 1: "))
    sq=num1**2
    print(f"Square of {num1} is {sq}")

def cube():
    num1=float(input("Enter number 1: "))
    cu=num1**3
    print(f"cube of {num1} is {cu}")

def mylog():
    num1=float(input("Enter number 1: "))
    f= math.log(num1)
    print(f"log of {num1} is {f}")

def expe():
    num1=float(input("Enter number 1: "))
    e=math.exp(num1)
    print(f"exponent of {num1} is {e}")
 
def sm():
    num1=int(input("Enter number 1: "))
    num2=int(input("Enter number 2: "))
    s=0
    for row in range(num1,num2+1):
        s=s+row
    print(f"Summision of {num1} and {num2} is {s}")
 
