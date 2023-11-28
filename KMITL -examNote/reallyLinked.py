class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        
class linked:
    def __init__(self):
        self.header = None
        
    def showlist(self):
        shower = self.header
        while shower:
            print(shower.data)
            shower = shower.next

lnk = linked()
lnk.header = node("monday")
e1 = node("tuesday")
e2 = node("wednesday")

lnk.header.next = e1
e1.next = e2

lnk.showlist()


        