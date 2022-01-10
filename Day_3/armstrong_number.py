#Program to check wheather the given number is amstrong or not.
user=int(input("enter a numbet to check weather a number is armstrong or not: " ) )
count=0
temp=rem=user
sum_=0
while user>0:
        user//=10
        count+=1

#print(user)
user=temp
while temp>0:
        rem=temp%10
        temp//=10
        sum_=sum_+rem**count

if sum_==user:
                print("armstrong")

else:
                print("not armstrong")

        
