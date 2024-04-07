tuple=(1,2,3)
print(tuple)
print(type(tuple))

t2=(10,)
print(t2)
print(type(t2))

t3=(1,2,5,7)
print(t3[0])
print(t3[1])
print(t3[2])
print(t3[3])
# out of range : print(t3[4])

# method-2 accessing tuple element

i=0
while i < len(t3):
      print(t3[i])
      i+=1
# method-3

for a in t3 :
      print(a)      

# built in methods in tuple
print(len(t3))
# min and max

print(min(t3))

print(max(t3))

# sum return sum of all value of tuple
print(sum(t3))

#sorted
print(sorted(t3))
print(sorted(t3, reverse=True))

print(t3*3)
print(t2+t3)

print(t3.index(5))
print(t3.count(5))

t5=(1,2,3,4,5,6,7,8)
print(t5[2:6:1])
print(t5[::-1])