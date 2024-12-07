# Reverse string:

def rev_by_recursion(string):
  if len(string)<=1:
    return string
  return rev_by_recursion(string[1:])+string[0]

def rev_by_loop(string):
  output=""
  for i in string:
    output=i+output
  return output

def rev_by_slicing(string):
  string=string[::-1]
  return string

if __name__=="__main__":
  string="ABCDEFG"
  print(rev_by_slicing(string))
  print(rev_by_loop(string))
  print(rev_by_recursion(string))