n=5
for i in range(1,n+1):
  for j in range(i):
      print("*",end=" ")
  print()
for i in range(n+1,2*n+1):
  for j in range(2*n-i):
    print("*",end=" ")
  print()
 