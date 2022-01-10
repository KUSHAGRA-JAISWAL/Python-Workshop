list_=[1,2,5,8,0]
list_a=['mohan','mohini']
list_b=[16,'yo']

for count in range(len(list_)):
    print(list_[count])
print("--")

for count in list_:
    print(count)
print("--")
print(list_[0:3])
print("--")
print(list_)
print("--")
list_[1]=20
print(list_)
print("--")
list_.insert(2,17)
print(list_)
print("--")
list_.append(51)
print(list_)
print("--")
list_[2:2]=[60,9,69]
print(list_)
print("--")
del list_[4]
print(list_)
print("--")
list_.remove(20)
print(list_)
print("--")
print(list_.remove(8))
print("--")
print(list_.index(5))
print("--")
print(list_.pop())
print("--")
print(list_a)
print("--")
print(list_b)
print("--")
print(list_[2])
print("--")
print(list_[-3])
print("--")
