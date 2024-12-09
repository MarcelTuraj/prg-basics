import queue
customer_queue = queue.Queue()
ticket = {}
id = 1
name_list = []
while True:
  name = input("Enter your name")
  name_list.append(name)
  if name == "STOP" :
    name_list.remove("STOP")
    break

for item in name_list:
  ticket[item] = id
  id += 1

for key, value in ticket.items():
  customer_queue.put(f"name: {key}, position in queue: {value}")

while not customer_queue.empty():
  print(customer_queue.get())
  
