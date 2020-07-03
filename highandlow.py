4.Write a function that checks whether a number is in a given range (inclusive of high and low)

In [10]:
def check_range(num,start,stop):
  if num in range(start,stop+1):
     print(num,"number is in a given range")
  else:
     print(num,"number is not in a Given range")