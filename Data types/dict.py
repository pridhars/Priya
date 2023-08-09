my_dict={
    1: "priya",
    2: "ringo",
}
print(my_dict)
even_odd={
    (2,4):(1,3),
    (6,8):(5,7),
}
print(even_odd)
my_dict={
    1: "priya",
    2: "ringo",
    3:["priya","ringo"]
}
print(my_dict)
my_dict = {        #length of the dictionary
    1: "priya",
    2: "ringo",
    3: ["priya","ringo"]
}
print(len(my_dict))
my_dict = {     #change element in dictonary
    1: "priya",
    2: "ringo",
    3: ["priya","ringo"]
}
my_dict["ringo"]=["bird"]
print(my_dict)
my_dict = {     #add element in a dictonary
    1: "priya",
    2: "ringo",
}
my_dict [3] =["priya","ringo"]
print(my_dict)
my_dict = {     #delete element in the dictonary
    "name" : "priya",
    2: "ringo",
    3: ["priya","ringo"]
}
del my_dict["name"]
print(my_dict)
my_dict = {     #clear element in the dictonary
    "name" : "priya",
    2: "ringo",
    3: ["priya","ringo"]
}
my_dict.clear()
print(my_dict)
my_dict = {     #pop element in the dictonary
    "name" : "priya",
    2: "ringo",
    3: ["priya","ringo"],
}
my_dict.pop(2)
print(my_dict)
marks={    #update in dictionary
    "chemistry":78,
    "physics":90,
}
internal_marks={
    "practical":80,
}
marks.update(internal_marks)
print(marks)
marks={    #clear a element in dictionary
    "chemistry":78,
    "physics":90,
}
marks.clear()
print(marks)
marks={    #key element in dictionary
    "chemistry":78,
    "physics":90,
}
dictionarykeys=marks.keys()
print(dictionarykeys)
marks={    #value element in dictionary
    "chemistry":78,
    "physics":90,
}
dictionarykeys=marks.values()
print(dictionarykeys)
marks={    #get element in dictionary
    "chemistry":78,
    "physics":90,
}
result = marks.get("chemistry")
print(result)
print(marks["physics"])
#popitem
my_dict = {
    "name" : "priya",
    2: "ringo",
    3: ["priya","ringo"],
}
result=my_dict.popitem()
print("return values",result)
print(my_dict)
#copy the element in dictionary
my_dict = {
    "name" : "priya",
    2: "ringo",
    3: ["priya","ringo"],
}
my_value=my_dict.copy()
print("my_dict",my_dict)
print("my_value",my_value)
