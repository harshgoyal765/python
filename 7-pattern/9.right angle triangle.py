for i in range (1,6):
  for j in range(5-i):
    print(" ",end=" ")
  for k in range(2*i-1):
    if k % 2 == 0:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  
  print()




  """
        * 
      *   * 
    *   *   * 
  *   *   *   * 
*   *   *   *   * 
   
"""