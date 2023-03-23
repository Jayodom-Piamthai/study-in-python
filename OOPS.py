class Ace:
    'this is me,deadass' #theese are the description of the class
    name ='Ace'
    mood = ''#and this is the attributes,this one is name
    def __init__(self,mood,activity): #this is "instance variable",with self as a pointer to the object
        self.mood = mood #making a new "object",this one named
        if activity in ["be productive"]:
            raise ValueError("Unacceptable bullshitery") #error exception of your own choosing
        self.activity = activity
    
    #string function
    def __str__(self): #return string
        return (f"apparently,because ace is {self.mood},he decided to {self.activity} today")

def main():
    ace = today()
    print(ace)
    
    
def today():
    mood = input("whats your mood today?:")
    activity = input("what'cha gon do today?:")
    return Ace(mood,activity)

if __name__ == "__main__":
    main()
