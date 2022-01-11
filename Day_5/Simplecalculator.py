#Program to show how to make a simple calculator.
import calop as cal
count=0
print("\n************************Welocome to our Calculator***************************\n")
print("--------------------To use this follow the instructions----------------------\n")
print("1 for Addition.\n")
print("2 for Substraction\n")
print("3 for Multiplication\n")
print("4 for Division\n")
print("5 for Square root\n")
print("6 for Factorial\n")
print("7 for Power\n")
print("8 for Square\n")
print("9 for Cube\n")
print("10 for log\n")
print("11 for Exponent\n")
print("12 for sumission\n")
print("0 for exit\n")

while True:
     key= int(input("\nEnter Any one Choice number: "))
     
     if key==1:
         cal.add()
     elif key==2: 
        cal.subs()

     elif key==3:
         cal.multy()

     elif key==4:
         cal.div()

     elif key==5:
         cal.mysqrt()

     elif key==6:
         cal.facto()

     elif key==7:
         cal.pow()

     elif key==8:
         cal.srq()

     elif key==9:
         cal.cube()

     elif key==10:
         cal.mylog()

     elif key==11:
         cal.expe()

     elif key==12:
         cal.sm()

     elif key==0:
         if count>0:
            print("\nThanks for using our calculator")
         else:
            print("\nYou wasted our hard work")
         break
     else:
         print("\nWrong Choice")
     count+=1
                   
        
