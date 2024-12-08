
from collections import Counter

def approach_1(string1,string2):
  
  if Counter(string1)==Counter(string2):
    return True
  else:
    return False

def approach_2(string1,string2):
  
  if sorted(string1) == sorted(string2):
    return True
  else:
    return False


if __name__=="__main__":
  string1="geeks"
  string2="kseeg"
  print(approach_1(string1,string2))
  print(approach_2(string1,string2))
