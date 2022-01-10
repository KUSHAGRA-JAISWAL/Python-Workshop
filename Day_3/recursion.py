n=int(input("Enter a number: "))
def calc(n):
                if n==1:
                                return 1
                return n*calc(n-1)
print(calc(n))
