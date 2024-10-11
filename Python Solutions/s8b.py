class Strings:
    def __init__(self):
        self.str = None

    def get_String(self):
        self.str = input("Enter String: ")

    def print_String(self):
        print(f"{self.str.upper()}")

    def reverseWord(self):
        strList = self.str.split()
        print("Each Word in the string in reverse order ")
        for e in strList:
            print(f"{e[::-1].lower()}")

str = Strings()
str.get_String()
str.print_String()
str.reverseWord()