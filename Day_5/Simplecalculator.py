#Program to show how to make a simple calculator.
import calop as cal
count=0
print("****Welocome to our Calculator****")
print("To use this follow the instructions")
print("1 for Addition")
print("2 for Substraction")
print("3 for Multiplication")
print("4 for Division")
print("5 for Square root")
print("6 for Factorial")
print("7 for Power")
print("8 for Square")
print("9 for Cube")
print("10 for log")
print("11 for Exponent")
print("12 for sumission")
print("0 for exit")

while True:
   
     
     key= int(input("Enter Any one Choice number: "))
     
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
            print("Thanks for using our calculator")
         else:
            print("You wasted our hard work")
         break
     else:
         print("Wrong Choice")
     count+=1
                   
        
