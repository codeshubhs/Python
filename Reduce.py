'''from functools import reduce
a=[10,20,30,40,50,100]

result= reduce(lambda n,m:n+m,a)
print(result)'''

# list and it's method

'''l1= [1,2,3,4]
x=l1.pop(2)
print(x)

del l1[0]
print(l1)

l1.remove(2)
print(l1)

l1.insert(2,5)
print(l1)
l1.reverse()
print(l1)

l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)
print(l1)
z=l1.index(4)
print(z)
l2=[10,11,14]
l2[0]=50
l1.extend(l2)
print(l1)'''


def student(firstname, lastname):
    print(firstname, lastname)
 
 
# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')