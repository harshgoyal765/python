for i in range (1,16):
   for j in range (1,16):
    if j==i or j==16-i:
      print("*" ,end=" ")
    else:
      print(" ",end=" ")
   print()


   """
*       * 
  *   *   
    *     
  *   *   
*       *
"""