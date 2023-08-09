#create a set in python
student_number={34,67,89,90,234}
print('student number:',student_number)
#empty set
x={}
print(x)
print(type(x))
#duplicate element in set
y={2,6,5,2,7,9,8,7.2}
print(y)
#add a element in set
name={'priyadharshini'}
name.add(20)
print(name)
#remove a element in set
name={'priyadharshini',98,'dharshini',39}
name.discard(98)
print(name)
#all
name={'priyadharshini',98,'dharshini',39}
result=all(name)
print(result)
#length of a set
name={'priyadharshini',98,'dharshini',39}
print(len(name))
