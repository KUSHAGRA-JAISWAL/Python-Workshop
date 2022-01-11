#Program to input the data of employee ad the concept of constructors.
class Employee:
   

    def __init__(__self__,name,designation,sallery):
      #  print("Creating Constructor")
        __self__.name=name
        __self__.designation=designation
        __self__.sallery=sallery

    def getName(__self__):
        return __self__.name
       

    def getDesignation(__self__):
        return __self__.designation

    def getSallery(__self__):
        return __self__.sallery        
       

emp_data=[]
while True:
    choice=input("\nEnter Choice (y) enter the data & (p) to print the data: ")
    if choice=='y':   
        u_name=input("\nEnter your name : ")
        u_deg=input("Enter your designation : ")
        u_sal=int(input("Enter your sallery : "))

        emp=Employee(u_name,u_deg,u_sal)
        emp_data.append(emp)


    elif choice=='p':
        for data in emp_data:
            print(f"\nEmployee name {data.getName()}\ndesignation {data.getDesignation()}\nsallery {data.getSallery()}\n")


    else:
        print("Exit..")
        break
