str = "Hello Team"
input = "".join(str[i] for i in range(len(str)) if i%2==0)
print(input)