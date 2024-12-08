from collections import Counter

def approach_2(string):
  return Counter(string)

def approach_1(string):
  count={}
  for i in string:
    if i in count:
      count[i]+=1
    else:
      count[i]=1
  return count

if __name__=="__main__":
  string="AAAABBBCCCDDDEFFFHSI"
  print(approach_1(string))
  print(approach_2(string))