# from collections import deque

# # Create a queue
# queue = deque()

# # Add people to the queue
# queue.append("Person 1")
# queue.append("Person 2")
# queue.append("Person 3")

# print("Queue:", queue)

# # Remove people (first come, first served)
# first = queue.popleft()
# print("First person served:", first)
# print("Queue after serving:", queue)


from collections import deque
queue = deque()

queue.append("person 1")
queue.append("person 2")
queue.append("person 3")

print("Queue:", queue)

queue.append("person 4")
queue.append("person 5")

first = queue.popleft()
print("First person serveed: ",first)
second = queue.popleft()
print("First person serveed: ",second)


print("Queue after serving:", queue)