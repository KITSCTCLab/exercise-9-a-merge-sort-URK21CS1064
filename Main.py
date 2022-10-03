from typing import List

def merge_sort(data,size) -> None:
  # Write code here
   for index in range(size):
    small_index = index
    for jindex in range(index+1, size):
      if array[jindex] < array[small_index]:
        small_index = jindex
    array[small_index],array[index] = array[index], array[small_index]
    return array

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(merge_sort(data,len(data)))
