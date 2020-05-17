from queue import Queue

q = Queue(maxsize=0)

q.put("Hello")
print(q.get())

print(q.empty())