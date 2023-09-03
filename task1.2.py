lst = ['0001','0011','0101','1011','1101','1111']

new_lst = [int(binary,2) for binary in lst]
print("new_lst = ",new_lst)
print(len(new_lst))

while len(new_lst)>2:
  x1=new_lst.pop(0)
  print(x1)
  x2=new_lst.pop(0)
  print(x2)
  sum = x1+x2
  new_lst.append(sum)
print("new_lst =",new_lst)