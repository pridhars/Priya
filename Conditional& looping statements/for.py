values=int(input("enter the number"))
for i in values:
    print(i)

#reverse the number using for loop
for i in range(100,0,-1):
    print(i)

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print("\n")
