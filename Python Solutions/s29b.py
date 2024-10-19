dict = {
    "kiwi": 7,
    "banana": 5,
    "apple": 3,
    "orange": 2,
}

sortByKeys = sorted(dict.items())
print(sortByKeys)

sortByKeysDesc = sorted(dict.items(), reverse=True)
print(sortByKeysDesc)

sortByValues = sorted(dict.items(), key=lambda x: x[1])
print(sortByValues)

sortByValuesDesc = sorted(dict.items(),key=lambda x: x[1], reverse=True)
print(sortByValuesDesc)