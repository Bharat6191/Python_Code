import re

def approach_1(string):
  regx=r'^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9]+$'

  if re.match(regx,string):
    return True
  else:
    return False

if __name__=="__main__":
  string="bharat.solanke@gmail.com"
  print(approach_1(string))
  # print(approach_2(string))