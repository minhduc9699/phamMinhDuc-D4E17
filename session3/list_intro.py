# List

quan_ao1 = 'hoodie'
quan_ao2 = 'ao phong'
quan_ao3 = 'quan bo'

list_quan_ao = ['hoodie', 'ao phong', 'quan bo', 'quần què']

list_quan_ao.append('áo ba lỗ')  # Create

index = list_quan_ao.index('quần què')  # find index of item

list_quan_ao[index] = 'áo mới' # update

removed_item = list_quan_ao.pop(0) # remove item and save it 
print(removed_item)

list_quan_ao.remove('quan bo') # remove by item value

if 'ao phong' in list_quan_ao: # check if item in list
    print('yeayy')

len_list_quan_ao = len(list_quan_ao)

for i in range(len_list_quan_ao): # Read all
    print('item', list_quan_ao[i]) # Read

for item in list_quan_ao: # Read all
    print(item)


# Create Read Update Delete
# print(list_quan_ao)

# print(quan_ao1)
# print(quan_ao2)
# print(quan_ao3)
