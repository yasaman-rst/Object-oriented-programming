queue = []

queue.append('Alice')
queue.append('Bob')
queue.append('Charlie')

print("Queue after enqueuing:", queue)

first_person = queue.pop(0)
print(f"{first_person} has been served.")

print("Queue after dequeuing:", queue)
