import string
def to_camel_case(text):
  alph = string.ascii_letters
  lst = list(text)
  if text=='':
    return ''
  for i in lst:
    if i not in alph:
      lst[lst.index(i)+1]=lst[lst.index(i)+1].upper()
      del(lst[lst.index(i)])

  print(''.join(lst))
  return ''.join(lst)



to_camel_case("vfd-vfdbfd_bdf_fdrff")