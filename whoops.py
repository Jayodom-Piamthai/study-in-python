class display():
    def __init__(self,number,stuff):
        self.number = number
        self.stuff =stuff
        number = 5 

class calculation():
    def __init__(self,what):
        self.what = what
    def add(x,y):
        return (x+y)
    def subtract(x,y):
        return (x - y)
    def multiply(x,y):
        return (x*y)
    def divide(x,y):
        return (x/y)
class A:
    def x(self):
        print("A")
class B(A):
    def x(self):
        print("B") 
        
           
class debtList():
    def __init__(self,name,amount,month):
       self.name = name
       self.amount = amount 
       self.month = month 
class listing(debtList):
    def __init__(self, name, amount,month):
        super().__init__(name, amount,month)
    def list(name,amount):
        return (str(name) + " has a total debt of" + str(amount))
    def list2(self):
        return (str(self.name) + " has a total debt of " + str(self.amount))
    
class reminder(debtList):
    def remind(self):
        return str(self.name)+"'s " +str(self.amount) +" baht debt is due in "+str(self.month)
Debt={("Ace",100),("Jay",500)}
Debt2=(100,200)
for i,j in Debt:
    print(listing.list(i,j))
    
test = listing("tester",1200,"december")
print (test.list2())
Ace = reminder("Ace",1500,"october")
print(Ace.remind())

print(calculation.add(300,55))
apple = 5
item = 'apples'
show = display(apple,item)
print(f"i have {show.number} {show.stuff}")
a = A()
b = B()
a.x()
b.x()