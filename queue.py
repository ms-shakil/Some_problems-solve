############## This is normal queue
class Queue:
    def __init__(self):
        self.items =[]

    def Enqueue(self,value):
        self.items.append(value)
    def Dequeue(self):
        if self.items == []:
            print("This queue is empty !")
        else:
            self.items.pop(0) 

My_q = Queue()
My_q.Enqueue("Shakil")
My_q.Enqueue("main")
My_q.Dequeue()
My_q.Dequeue()
My_q.Dequeue()
print(My_q.items)


##############3 circular queue

class C_queue:
    def __init__(self,length):
        self.item = [0] * length
        self.max_length = length
        self.left,self.right,self.size = 0,0,0


    def Enqueue(self,value):
        if self.size == self.max_length:
            print("This queue is full")
            return
        else:
            self.item[self.right] = value
            self.right = (self.right +1) % self.max_length
            self.size +=1

    def  Dequeue(self):
        if self.size == 0:
            print("This queue is  empty:")
            return
        else:
            item = self.item[self.left]
            self.left = (self.left +1) % self.max_length
            self.size  -=1
            return item

My_Cqueue = C_queue(5)
My_Cqueue.Enqueue("Shakil")
My_Cqueue.Enqueue("Shakil")
My_Cqueue.Enqueue("Shakil")
My_Cqueue.Enqueue("Shakil")
My_Cqueue.Enqueue("payer")
My_Cqueue.Dequeue()
My_Cqueue.Enqueue("main")
My_Cqueue.Enqueue("fahad")
print(My_Cqueue.item)
print(My_Cqueue.left,My_Cqueue.right)








