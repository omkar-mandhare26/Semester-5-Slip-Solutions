class ValidateParentheses:
    def __init__(self, str):
        self.str = str
    
    def validate(self):
        stk = []
        parentheses = { "(": ")","[": "]","{": "}"}
        
        for char in self.str:
            if char in parentheses.keys():
                stk.append(char)
            elif char in parentheses.values():
                opening = stk.pop()

                if char != parentheses[opening]:
                    return False
                else:
                    continue
                
        if len(stk) == 0:
            return True
        else:
            return False

s = "(asdsa[asdsa]asdsa {asdsa})"

obj = ValidateParentheses(s)
result = obj.validate()

if result:
    print("Parentheses are valid")
else:
    print("Parentheses are not valid")