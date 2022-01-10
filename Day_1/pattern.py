#Program to show how to create a square pattern using loops.
print("********")
print("********")
print("********")
print("********")
print("********")

print("---------")

for row in range(5):
    print("********")

print("---------")

for row in range(5):
    for col in range(5):
        print("*" , end=" ")
    print()
