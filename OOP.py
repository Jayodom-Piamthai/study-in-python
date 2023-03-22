class Ace:
    'this is me,deadass' #theese are the description of the class
    name ='Ace'
    mood = ''#and this is the attributes,this one is name
    def __init__(self,mood,activity): #this is "instance variable",with self as a pointer to the object
        self.mood = mood #making a new "object",this one named
        if activity in ["be productive"]:
            raise ValueError("Unacceptable bullshitery")
        self.activity = activity

def main():
    ace = today()
    print(f"today ace is {ace.mood},and he's gonna {ace.activity}")
    
def today():
    mood = input("whats your mood today?:")
    activity = input("what'cha gon do today?:")
    return Ace(mood,activity)


main()
