class Employee:
    #n=k

    def __init__(__self__,name,designation,sallery):
        print("Creating Constructor")
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
    choice=input("Enter Choice")
    if choice=='y':   
        u_name=input("Enter your name : ")
        u_deg=input("Enter your designation : ")
        u_sal=int(input("Enter your sallery : "))

        emp=Employee(u_name,u_deg,u_sal)
        emp_data.append(emp)


    elif choice=='p':
        for data in emp_data:
            print(f"Employee name {data.getName()},designation {data.getDesignation}and sallery {data.sallery}")


    else:
        break
