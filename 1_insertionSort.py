def insertSort(lst):
  for index, v in enumerate(lst[1:]):
      while (index >= 0) and (v < lst[index]):
          lst[index+1] = lst[index]
          lst[index] = v
          index -= 1

lst = [ 4, 1, 8, 2, 6, 12, 5]
insertSort(lst)
print(lst)
