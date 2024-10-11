list = []
n = int(input("Enter No of Elements: "))
for i in range(0,n):
    e = int(input(f"Enter Element {i+1}: "))
    list.append(e)

print(f"Before Removing Duplicates: {list}")

newList = []
for i in list:
    if i not in newList:
        newList.append(i)

print(f"After Removing Duplicates: {newList}")