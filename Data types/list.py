x=[1,2,3,4,6,9]
print(x)
x=0.98
print(type(x))  #data type
x=[1,2,3,4,6,9]
print(type(x))
x=[1,2,3,4,6,9]
print(x[1:])     #silcing operator
print(x[-2:3])
x[2]=7
print(x)
fruits=["apple","orange","graps"]
fruits.append("pineapple")     #append a list
print(fruits)
fruits.extend("pineapple")    #extend a list
print(fruits)
fruits=["apple","orange","graps"]
fruits.insert(2,"pineapple")  #insert a list
print(fruits)
fruits=["apple","orange","graps"]
del fruits[1]    #delete a element in list
print(fruits)
fruits=["apple","orange","graps"]
fruits.remove("graps")    #remove a element in list
print(fruits)
p=[]   #empty list
print(p)
fruits=["apple","orange","graps","pineapple"]
remove_element=fruits.pop()  # pop a element in list
print(remove_element)
fruits=["apple","orange","graps","pineapple"]
fruits.clear()  #clear a list
print(fruits)
numbers = [2, 3, 5, 2, 11, 2, 7]
count=numbers.count(9)  #cout a element in list
print(count)
numbers = [2, 3, 5, 2, 11, 2, 7]
numbers.sort()    # sort the element in list
print(numbers)
