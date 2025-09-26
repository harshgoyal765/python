n=5
for i in range(0,5):
  for j in range(n-i,1,-1):
    print(j,end=" ")
  print("*",end=" ")
  for k in range(i,0,-1):
    print(k, end=" ")
  print()



  """
5 4 3 2 * 
4 3 2 * 1 
3 2 * 2 1 
2 * 3 2 1 
* 4 3 2 1 
"""