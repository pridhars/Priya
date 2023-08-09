#pattern
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print()
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print()

#pattern numbers
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
#pattern reverse
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print("")
#pattern reverse numbers
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
