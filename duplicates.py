2.Write a Python program to remove consecutive duplicates from list

In [64]:
mylist=[2,5,5,6,6,9,3]
prev=None
newlist=[]
for item in mylist:
  if item!=prev:
        newlist.append(item)
        prev=item
print("The new list:\n")
print(newlist)