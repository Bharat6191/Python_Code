


def approach_1(string):
  vowel=['A','E','I','O','U','a','e','o','i','u']
  replace="@"
  s=""
  for i in string:
    if i in vowel:
      s+=replace
    else:
      s+=i
  return s


if __name__=="__main__":
  string="asdfghjklqwertyuiopmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM"
  print(approach_1(string))