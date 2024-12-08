#Count the number of words in a string.
def approach_2(string):
  return len(string.split(" "))

def approach_1(string):
  if len(string)==0:
    return 0
  w=1
  for i in string:
    if i==" ":
      w+=1
  return w

if __name__=="__main__":
  string="AAAA BBB CCC DDD EFF FH S I"
  print(approach_1(string))
  print(approach_2(string))