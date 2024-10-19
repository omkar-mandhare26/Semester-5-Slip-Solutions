str = "Hello World!"
cipherText = ""
shift = 2
for char in str:
    if char.isalpha():
        cipherText += chr(ord(char) + shift)
    else:
        cipherText += char
    
print(cipherText)