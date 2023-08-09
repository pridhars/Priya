#lambda
a=lambda:print("priyadharshini")
a()
#using filter function
my_list=[1,2,4,5,6,7,8,9]
new_list=list(filter(lambda a:(a%2!=0),my_list))
print("a=",new_list)
numbers=[1,2,3,4,5,6,7,8,9]
even_numbers=filter(lambda x:(x%2==0),numbers)
even_numbers=list(even_numbers)
print("even numbers",even_numbers)
#Using None as a Function Inside filter()
random_list = [1, 'a', 0, False, True, '0']
filtered_iterator = filter(None, random_list)
filtered_list = list(filtered_iterator)
print(filtered_list)
#using map function
num1 = [4, 5, 6]
num2 = [5, 6, 7]
result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))
#using reduce function
from functools import reduce
mylist = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, mylist)
print(product)
