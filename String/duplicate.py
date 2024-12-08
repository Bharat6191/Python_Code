
def approach_1(string):
  s=set(string)
  return str(s)

def approach_2(string):
  s=""
  for i in string:
    if i in s:
      continue
    else:
      s+=i
  return s

if __name__=="__main__":
  string="geeks"
  # print(approach_1.__doc__)
  print(approach_1(string))
  print(approach_2(string))