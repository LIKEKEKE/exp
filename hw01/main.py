for i in range(1,10):
  for n in range(1,i):
      print(end='         ')
  for j in range(i,10):
    print('%d * %d=%2d'%(j,i,j*i),end=' ')
    
  print('\n')
  
