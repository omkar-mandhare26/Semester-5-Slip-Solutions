class ReverseString:
    def __init__(self, string):
        self.str = string
    
    def reverse(self):
        words = str.split()
        reversedWords = words[::-1]
        return " ".join(reversedWords)

str = "Hello World! This is a test for reversing a string word by word"

print(f"Original string: {str}")

obj = ReverseString(str)
reversedString = obj.reverse()

print(f"Reversed string: {reversedString}")