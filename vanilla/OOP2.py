
## inheritance -> other class can inherits from another class ,so if class B with inheritance from class A
# also gets inherits by class C , that class will inherits BOTH class A and B
# A -> B(A) -> C(B) = C(B,A) 
class Grandpa:
    lastName = 'ancestorson' #class variable;every class inherited,object instantiate from this class will have this lastname
    def __init__(self,Name):
        self.Name = 'gerald'
        
    def theWar(self):
        print('war never changes')
    
class pappy(Grandpa):
    def theDepression(self):
        print('and then the market crashed,along with every skulls against the floor')
        
class Sonny(pappy):
    def theRot(self):
        print('SIX SEVENNNNNNNN')
        
sunny = Sonny('sunny')
sunny.theRot()
sunny.theDepression()
sunny.theWar()
print(sunny.lastName)