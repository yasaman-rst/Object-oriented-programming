class Task:           #P1
 id_counter =1

 def __init__(self,description,programmer,workload) :
  self.id = Task.id_counter
  Task.id_counter += 1  # Unique ID 
  self.description = description
  self.programmer = programmer
  self.workload = workload
  self.finished = False  # New tasks are not finished

 def is_finished(self):
        return self.finished

 def mark_finished(self):
        self.finished = True

 def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"
 #example:
t1 = Task("program hello world", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())

t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)

print(t2)
print(t3)

class OrderBook:    #P2() with added functions )
     def __init__(self) :
          self.orders = []

     def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

     def all_orders(self):
        return self.orders  # Returns all stored Task objects

     def programmers(self):
        return list(set(order.programmer for order in self.orders))  # Unique programmer names
     def get_order(self, id):
        for order in self.orders:
            if order.id == id:
                return order
        return None  # Return None if no task with is found  
     
     def mark_finished(self, id: int):
        task = self.get_order(id)
        if task is None:
            print(f"No task with id {id}")
        else:
            task.mark_finished()
     
     def finished_orders(self): #new features
        return [order for order in self.orders if order.is_finished()]

     def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

      
          


#example:
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

orders.mark_finished(1)
orders.mark_finished(2)
for order in orders.all_orders():
    print(order)
print()

for programmer in orders.programmers():
    print(programmer)
my_list = [1,1,3,6,4,1,3]
my_list2 = list(set(my_list))
print(my_list)
print(my_list2)