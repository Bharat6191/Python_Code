# from reverse import rev_by_recursion

def rev_by_recursion(string):
  if len(string)<=1:
    return string
  return rev_by_recursion(string[1:])+string[0]


if __name__=="__main__":
  string="ABCBA"
  if string==rev_by_recursion(string):
    print("True")
  else:
    print("False")





