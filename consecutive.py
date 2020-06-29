x = [1,2,4,7,3,7,8,4,4,9]
previous_value = None
new_lst = []
for elem in x:
   if elem != previous_value:
       new_lst.append(elem)
       previous_value = elem
print(new_lst)