def TreeConstructor(strArrlist2):

  '''
  Determine if list of quoted tuples is valid construction of binary tree.

  list of quoted tuples --> string
  '''  
  # code goes here
 
  parents = {}

  for i in range(len(strArrlist2)):
      if strArrlist2[i][3] in parents:
          if parents[strArrlist2[i][3]][1]:
              return 'false'
          else:
              parents[strArrlist2[i][3]][1] = strArrlist2[i][1]
      else:
          parents[strArrlist2[i][3]] =  [None] * 2 
          parents[strArrlist2[i][3]][0] = strArrlist2[i][1]

  return 'true'

# keep this function call here 
print(TreeConstructor(input())
