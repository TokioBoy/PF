def unique_in_order(iterable):
  lst = list(iterable)
  res = []
  for i in range(len(lst)):
    if i == 0:
      res.append(lst[i])
    elif lst[i] != lst[i-1]:
      res.append(lst[i])
  print(res)
  return res
unique_in_order('AAAABBBCCDAABBB')