import decimal as D
import fractions as fr

var1=5
var2=1.9
var3='6+7'

var4= complex(var2)

var5=D.Decimal(5.3)
var6=fr.fractions(3.3)

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var4.real))

print(type(var5))
print(var5)
print(var6)
