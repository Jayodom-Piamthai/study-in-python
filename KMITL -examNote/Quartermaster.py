class Q:
    def __init__(self,max):
        self.max = max
        self.queue = []
        self.front = 0
        self.rear = -1
        
    def enQ(self,num):
        if self.rear < self.max-1:
            self.queue.append(num)
            print(f"successfully queued {num}")
            self.rear += 1
        else:
            print("ERROR,queue full")
    
    def deQ(self):
        temp = self.queue[self.front]
        l = len(self.queue)
        for i in range(l- 1):
            self.queue[i] = self.queue[i+1]
        self.rear -= 1
        self.queue.pop()
        print(f"dequeue {temp} successfully")
        
    
    def show(self) :
            print (self.queue)
    
    def get(self,pos):
        if self.front > self.rear :
            print("ERROR,queue empty")
        else :
            print(self.queue[pos])

q = Q(3)

q.enQ(3)
q.enQ(6)
q.enQ(9)
q.enQ(13)
q.enQ(15)
q.show()
q.deQ()
q.show()
q.enQ(12)
q.show()

