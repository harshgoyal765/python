n=5
for i in range(1,n+1):
  for j in range(2*i-1):
    if j%2!=0:
      print("!",end=" ")
    else:
      print(i,end=" ")
  print()
for i in  range(n+1,1,-1):
  for j in range(2*i-n):
    if j%2!=0:
      print("!",end=" ")
    else:
      print(i-2,end=" ")
  print()



"""
1 
2 ! 2 
3 ! 3 ! 3 
4 ! 4 ! 4 ! 4 
5 ! 5 ! 5 ! 5 ! 5 
4 ! 4 ! 4 ! 4 
3 ! 3 ! 3 
2 ! 2 
1
"""