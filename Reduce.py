from functools import reduce
a=[10,20,30,40,50,100]

result= reduce(lambda n,m:n+m,a)
print(result)