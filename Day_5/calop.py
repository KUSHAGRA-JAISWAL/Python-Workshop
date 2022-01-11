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
    num1=float(input("\nEnter number 1: "))
    num2=float(input("\nEnter number 2: "))
    sum_=num1+num2
    print(f"\nsum of {num1} and {num2} is {sum_}")

def subs():
    num1=float(input("\nEnter number 1: "))
    num2=float(input("\nEnter number 2: "))
    sub=num1-num2
    print(f"\nsubstraction of {num1} and {num2} is {sub}")

def multy():
    num1=float(input("\nEnter number 1: "))
    num2=float(input("\nEnter number 2: "))
    mul=num1*num2
    print(f"\nMultiplication of {num1} and {num2} is {mul}")

def div():
    num1=float(input("\nEnter number 1: "))
    num2=float(input("\nEnter number 2: "))
    dive=num1/num2
    print(f"\nDivision of {num1} and {num2} is {dive}")

def mysqrt():
    num1=float(input("\nEnter number : "))
    res=math.sqrt(num1)
    print(f"\nsquareroot of {num1} is {res}")
    
def facto():
    num1=int(input("\nEnter number : "))
    f=math.factorial(num1)
    print(f"\nsquareroot of {num1} is {f}")

def pow():
    num1=float(input("\nEnter number 1: "))
    num2=float(input("\nEnter number 2: "))
    pow_=num1**num2
    print(f"power of {num1} and {num2} is {pow_}")
   
def srq():
    num1=float(input("\nEnter number : "))
    sq=num1**2
    print(f"\nSquare of {num1} is {sq}")

def cube():
    num1=float(input("\nEnter number : "))
    cu=num1**3
    print(f"\ncube of {num1} is {cu}")

def mylog():
    num1=float(input("\nEnter number : "))
    f= math.log(num1)
    print(f"\nlog of {num1} is {f}")

def expe():
    num1=float(input("\nEnter number 1: "))
    e=math.exp(num1)
    print(f"\nexponent of {num1} is {e}")
 
def sm():
    num1=int(input("\nEnter number 1: "))
    num2=int(input("\nEnter number 2: "))
    s=0
    for row in range(num1,num2+1):
        s=s+row
    print(f"\nSummision of {num1} and {num2} is {s}")
 
