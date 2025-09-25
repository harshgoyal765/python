n=7
a=n//2+1

for i in range(1,a+1):
  for j in range(a-i):
    print("*",end=" ")
  for k in range(2*i):
    print(" ",end=" ")
  for l in range(a-i):
    print("*",end=" ")
  print()
for i in range(a+1,n+1):
  for j in range(i-a):
    print("*",end=" ")
  for k in range((2*a-i)*2):
    print(" ",end=" ")
  for l in range(i-a):
    print("*",end=" ")
  print()



"""
* * *     * * * 
* *         * * 
*             * 
                
*             * 
* *         * * 
* * *     * * * 
"""