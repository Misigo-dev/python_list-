#empty list
my_list = []
# appending numbers 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list) 
# inserting 15 at index 1 
my_list.insert(1, 15)
print(my_list) 
# extending the list with 50,60,70 
my_list.extend([50, 60, 70])
print(my_list)
# removing 70 from the list
my_list.remove(70)  
print(my_list)
# sorting the list in ascending order
asc = sorted(my_list)
print( "Ascending order:", asc)
# sorting the list in descending order
desc = sorted(my_list, reverse=True)
print("Descending order:", desc)
# finding the index of 30
idx = my_list.index(30)
print("Index of 30:", idx)