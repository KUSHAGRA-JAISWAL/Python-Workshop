#Python program to demonstrate diamond pattern using different number of loops.

n = int(input("Enter a number for Diamond pattern : ")) #n=5

print("Diamond Pattern") #diamond patter usin 8 loops.
"""
          *
        * * *
      * * * * *
    * * * * * * *
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
    print(" ")

for row in range(n):
    for col in range(row+1):
        print(" " , end=" ")

    for col in range(row,n-1):
        print("*" , end=" ")
    for col in range(row,n):
        print("*",end=" ")    
    print(" ")

print("--------------------------------")

print("Diamond Pattern") #diamond patter usin 6 loops.
"""
           *
         *   *
       *   *   *
     *   *   *   *
   *   *   *   *   *
     *   *   *   *
       *   *   *
         *   *
           *

"""

for row in range(n-1):
    for col in range(row,n):
       print(" " , end=" ")

    for col in range(row+1):
        print(" * " , end=" ")
    
    print(" ")

for row in range(n):
    for col in range(row+1,):
        print(" " , end=" ")

    for col in range(row,n):
        print(" * " , end=" ")
      
    print(" ")

print("--------------------------------")

print("Diamond Pattern") #diamond patter usin 4 loops.
"""
           *
         *   *
       *   *   *
     *   *   *   *
   *   *   *   *   *
     *   *   *   *
       *   *   *
         *   *
           *

"""
#for row in range(n,row)

print("--------------------------------")

print("Diamond Pattern") #diamond patter usin 2 loops.
"""
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *

"""
for row in range(n+1):
    print(" "*(n-row)+" *"*row)

for row in range(n-1,0,-1):
   print(" "*(n-row)+" *"*row)