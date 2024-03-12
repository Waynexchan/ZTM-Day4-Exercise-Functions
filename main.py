
def highest_even(li):
  even_list = []
  for item in li:
    if item % 2 == 0:
      even_list.append(item)
  return max(even_list)
print(highest_even([10,2,3,4,8,11]))