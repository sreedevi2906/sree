5.Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters. Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?' Expected Output : No. of Upper case characters : 4 No. of Lower case Characters : 33

In [52]:
def char_test(s):
  uppercase,lowercase,special=0,0,0
  for char in s:
    if char.isupper():
        uppercase+=1
    elif char.islower():
        lowercase+=1
    else:
        special+=1
  print("number of uppercase characters=",uppercase)
  print("number of lowercase characters=",lowercase)
  print("number of special characters=",special)