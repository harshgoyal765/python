n=5
for i in range(1,n+1):
  for j in range(n+1-i):
    print(" ",end=" ")
  for k in range (i):
    print("*",end=" ")
  print()
for i in range(n+1,2*n+1):
  for j in range(i-n+1):
    print(" ",end=" ")
  for k in range(2*n-i):
    print("*",end=" ")
  print() 



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