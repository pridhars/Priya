#empty tuple
p=()
print(p)
tuple = ("mouse", [8, 4, 6], (1, 2, 3))   #nested tuple
print(tuple)
a=("priya",) #tuple /comma to indicate that it is a tuple
print(type(a))
b=("priya",2,(2,6,8),9)  #indexing
print(b[3])
b=("priya",2,(2,6,8),9)
print(b[-2])#negative indexing
b=("priya",2,(2,6,8),9)    #silcing
print(b[1:])
b=("priya",2,2,6,8,5,9,0,4,9)  #count
print(b.count(2))
b=("priya",2,(2,6,8),9)  #checking
print(8 in b)
b=("priya",2,(2,6,8),9)
print(2 in b)
