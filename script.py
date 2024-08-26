todo_list = []

while True:
  if len(todo_list) == 0:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1

  print("Options:")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. Quit")

  choice = input()
  if choice == "1":
    new_task = input("Add your task: ")
    todo_list.append(new_task)
    print("Task has been added")
  elif choice == "2":
    if len(todo_list) == 0:
      print("ToDo list empty")
    else:
      todo_list.pop()
  else:
    print("Quitting")
    break