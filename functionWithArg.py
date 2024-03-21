'''def add(y) :
    x=10
    c=x+y
    print(c)
    
add(20)   '''
# normal function 
'''def show (x):
    return x
print(show(5))'''

#lamda function 
show = lambda x :print(x)
show(5)

add = lambda x,y : x+y
print(add(8,9))

add_sub = lambda a,b: (a+b, a-b)
z,p= add_sub(8,6)
print(z)
print(p)

sub = lambda x1,x2=4 : x1-x2
print(sub(8))