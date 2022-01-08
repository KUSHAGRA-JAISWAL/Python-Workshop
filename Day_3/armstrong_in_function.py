

user=int(input("enter a numbet to check weather a number is armstrong or not: " ) )
def arm(user):
                n=user
                count=0
                temp=rem=user
                sum_=0
                while user>0:
                        user//=10
                        count+=1

                #print(user)
                store=temp
                while temp>0:
                        rem=temp%10
                        temp//=10
                        sum_=sum_+rem**count

                if sum_==store:
                                print("armstrong")

                else:
                                print("not armstrong")

arm(user)      
