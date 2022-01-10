import decimal as D
import fractions as fr
import math as m

a=10 #global
def test(c):
    global b=12 #local
    print(a)
    print(b)

print(a)
print(b)
print(m.pi)
print(m.exp(10))
print(m.sin(90))
print(m.factorial(6))
