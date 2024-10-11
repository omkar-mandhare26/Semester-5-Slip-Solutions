dict = {
    "Martin": 14,
    "Avicii": 8,
    "KSHMR": 18,
    "Omkar": 4
}

keyToCheck = input("Enter Key to Check: ")

print(f"Old Dictionary: {dict}")
if keyToCheck in dict.keys():
    print("Key Exists in the Dictionary")
    
    newKey = input("Enter New Key: ")
    newValue = int(input("Enter New Value: "))
    
    dict.pop(keyToCheck)
    dict[newKey] = newValue

print(f"New Dictionary: {dict}")