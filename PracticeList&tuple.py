#wap to ask the user enter names of their 3 favorite movies
#and store them in a list

'''movie1=input("enter your favotite movie:")
movie2=input("enter your favotite movie:")
movie3=input("enter your favotite movie:")

#print(movie1)
#print(movie2)
#print(movie3)

list=[movie1, movie2, movie3]

print(list)'''

'''movies=[]

movie1=input("enter your favotite movie:")
movie2=input("enter your favotite movie:")
movie3=input("enter your favotite movie:")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)'''
#2. wap to check if a list contains a pallindrome
#of elements.(Hint: use copy method)

'''list1=[1,2,1]
copy_list= list1.copy()
copy_list.reverse()

if(copy_list==list1):
    print("Pallindrome")
else:
    print("Not pallindromw")'''

#3
grade=["C","D","A","A","B","B","A"]

print(grade.count("A"))

grade.sort()
print(grade)