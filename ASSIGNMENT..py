 #Remove duplicates from the list without using set() in python.
i=1
my_list =[1,2,2,3,4,5,7,8,9]
new_list=[]
for i in my_list:
  if i not in new_list:
    new_list.append(i)
print(my_list)
print(new_list)
 
 
 # Add two matrix
a=[[1,2], [3,4]]
b=[[4,3],[2,1]]
for i in a:
 print(i)
 for i in b:
  print(b)
for i in range(1):
 for j in range(1):
  c=a[i][j]+b[i][j]
print("The sum of two  matrix is :" ,c)


# Multiplication of two matrix
a=[[1,2], [3,4]]
b=[[4,3],[2,1]]
for i in a:
 print(i)
 for i in b:
  print(b)
for i in range(1):
 for j in range(1):
  c=a[i][j]*b[i][j]
print("The MULTIPLICATION OF  two  matrix is :" ,c)



