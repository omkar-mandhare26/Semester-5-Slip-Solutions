str = "The Quick Brown Fox"
upperCount = 0
lowerCount = 0
for ch in str:
    if ch.isupper():
        upperCount += 1
    elif ch.islower():
        lowerCount += 1

print(f"Count of Upper Chars: {upperCount}")
print(f"Count of Lower Chars: {lowerCount}")