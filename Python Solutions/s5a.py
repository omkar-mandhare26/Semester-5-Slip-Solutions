class Strings:
    def __init__(self):
        self.str = None
    
    def get_String(self):
        self.str = input("Enter String: ")
    
    def print_String(self):
        print(f"String in Upper Case: {self.str.upper()}")

StringsObj = Strings()
StringsObj.get_String() 
StringsObj.print_String() 