class Country:
    def __init__(self):
        self.nationality = ""

    def acceptNationality(self):
        self.nationality = input("Enter your nationality: ")

    def printNationality(self):
        print(f"Nationality: {self.nationality}")

class State(Country):
    def __init__(self):
        super().__init__()
        self.state = ""

    def acceptState(self):
        self.state = input("Enter your state: ")

    def printState(self):
        print(f"State: {self.state}")

    def printInfo(self):
        print(f"State: {self.state}, Country: {self.nationality}")

state = State()

state.acceptNationality()
state.acceptState()

state.printNationality()
state.printState()

state.printInfo()
