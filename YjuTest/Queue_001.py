

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(6)
queue.popleft()

print(queue)
queue.reverse()
print(queue)


