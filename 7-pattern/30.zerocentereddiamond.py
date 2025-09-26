

n=10

for i in range(0,n):
  for j in range(n-i-1,0,-1):
    print(" ",end=" ") 
  for k in range(n-i,n):
    print(k,end=" ")
  print("0",end=" ") 
  for l in range(n-1,n-i-1,-1):
    print(l,end=" ")

  print()



"""
                  0 
                9 0 9 
              8 9 0 9 8 
            7 8 9 0 9 8 7 
          6 7 8 9 0 9 8 7 6 
        5 6 7 8 9 0 9 8 7 6 5 
      4 5 6 7 8 9 0 9 8 7 6 5 4 
    3 4 5 6 7 8 9 0 9 8 7 6 5 4 3 
  2 3 4 5 6 7 8 9 0 9 8 7 6 5 4 3 2 
1 2 3 4 5 6 7 8 9 0 9 8 7 6 5 4 3 2 1 
"""