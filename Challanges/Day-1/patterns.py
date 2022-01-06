#Python program to print different patterns by taking input from the user.

n = int(input("Enter a number for pattern : "))

print("Increasing Trangle")
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * *         
* * * * * * *       
* * * * * * * *     
* * * * * * * * *   
* * * * * * * * * * 
"""
for row in range(n):
    for col in range(row):
        print("*" , end=" ")
    print()

print("------------------------------")

print("Right Sided Trangle")

"""
                      *
                    * *
                  * * *
                * * * *
              * * * * *
            * * * * * *
          * * * * * * *
        * * * * * * * *
      * * * * * * * * *
    * * * * * * * * * *
  * * * * * * * * * * *

"""

for row in range(n):
    for col in range(row,n):
        print(" " , end=" ")

    for col in range(row+1):
        print("*" , end=" ")
    print()

print("------------------------------")

print("Decreasing Trangle")

"""
  * * * * * * * * * * *
    * * * * * * * * * *
      * * * * * * * * *
        * * * * * * * *
          * * * * * * *
            * * * * * *
              * * * * *
                * * * *
                  * * *
                    * *
                      *

"""


for row in range(n):
    for col in range(row+1):
        print(" " , end=" ")

    for col in range(row,n):
        print("*" , end=" ")
    print()

print("------------------------------")

print("Hill pattern")

"""
                      *
                    * * *
                  * * * * *
                * * * * * * *
              * * * * * * * * *
            * * * * * * * * * * *
          * * * * * * * * * * * * *
        * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * *
  * * * * * * * * * * * * * * * * * * * * *
"""


for row in range(n):
    for col in range(row,n):
        print(" " , end=" ")

    for col in range(row):
        print("*" , end=" ")
    for col in range(row+1):
        print("*",end=" ")    
    print()

print("------------------------------")

print("Reverse Hill pattern")

"""
  * * * * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * *
      * * * * * * * * * * * * * * * * *
        * * * * * * * * * * * * * * *
          * * * * * * * * * * * * *
            * * * * * * * * * * *
              * * * * * * * * *
                * * * * * * *
                  * * * * *
                    * * *
                      *
"""


for row in range(n):
    for col in range(row+1):
        print(" " , end=" ")

    for col in range(row,n-1):
        print("*" , end=" ")
    for col in range(row,n):
        print("*",end=" ")    
    print()

print("------------------------------")

print("Diamond Pattern")
"""
                *
              * * *
            * * * * *
          * * * * * * *
        * * * * * * * * *
      * * * * * * * * * * *
    * * * * * * * * * * * * *
  * * * * * * * * * * * * * * *
    * * * * * * * * * * * * *
      * * * * * * * * * * *
        * * * * * * * * *
          * * * * * * *
            * * * * *
              * * *
                *

"""

for row in range(n-1):
    for col in range(row,n):
        print(" " , end=" ")

    for col in range(row):
        print("*" , end=" ")
    for col in range(row+1):
        print("*",end=" ")    
    print()

for row in range(n):
    for col in range(row+1):
        print(" " , end=" ")

    for col in range(row,n-1):
        print("*" , end=" ")
    for col in range(row,n):
        print("*",end=" ")    
    print()