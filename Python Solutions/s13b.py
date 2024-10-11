class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) 
        else:
            return "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue: ", q.queue)

print("Queue: ", q.dequeue())
print("Queue: ", q.queue)

q.dequeue()
q.dequeue()
print("Queue: ", q.dequeue())