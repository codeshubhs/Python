# filter

a = [10, 20, 30, 40, 50, 70]

def high_marks(n):
    if n>=20 :
        return True

   # we can print in this way  
result= filter(high_marks, a)
for el in result :
    print(el)

    # also in this way 
'''result=list(filter(high_marks,a))
print(result)'''

# map 
b=[20,35,49,58,60,70]
'''def inc(n1) :

    return n1+2'''
'''ans = map(lambda n1 : n1+5,b)
for i in ans :
    print(i)'''

ans = map(lambda n1,m1 : n1+m1,a,b)
for i in ans :
    print(i)
