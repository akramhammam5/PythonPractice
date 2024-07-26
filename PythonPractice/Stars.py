#Considering this as a GUI Image
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0],
]


for i in picture:
  for j in i:
     if j == 1:
      print('*',end='')
     else:
      print(' ',end='')
  print('\n')

