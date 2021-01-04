#set
b={}
b=set(b)
print(type(b))
#adding values to empty set
b.add(4)
b.add(6)
# b.add(4)
# b.add(4)
# b.add(6)
#set is non repeative so how many times i add 4 or 6 it will print only 1 time
b.add((4,4,5))#we can add tuple
# b.add({4:5})#error as we cannot add dic to sets 
print(b)
# print(len(b))# tells u item
#removal _--__--...>>>>>>>>>>>>>>>>>>>>>
b.remove(6)
print(b)

print(b.pop())
print(b)