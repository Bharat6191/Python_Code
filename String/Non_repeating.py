# Find the first non-repeating character in a string.


def approach_2(string):
  for i in string:
    if string.count(i)==1:
      return i
  return False

def approach_1(string):
  dic={}
  for i in string:
    if i in dic:
      dic[i]=dic[i]+1
    else:
      dic[i]=1
  for i in dic:
    if dic[i]==1:
      return i
  return False

if __name__=="__main__":
  string="AAAABBBBBBCCCCCDDDE"
  print(approach_1(string))
  print(approach_2(string))
  