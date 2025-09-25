n=5
for i in range (1,n+1):
  for j in range(2*i-2):
    print(" ",end=" ")
  for k in range(n+1-i):
    print("*",end=" ")
  print()
for i in range(n+1,2*n):
  for j in range((2*n-i)*2-2):
    print(" ",end=" ")
  for k in range(i-n+1):
    print("*",end=" ")
  print()


  """
* * * * * 
    * * * * 
        * * * 
            * * 
                * 
            * * 
        * * * 
    * * * * 
* * * * *
"""