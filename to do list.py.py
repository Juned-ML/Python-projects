print("this is a to do list program")
task = []

def add_task():
  task.append(input("enter the taask to add :"))
  i = 0
  for i in task:
    print("task added")


def remove_task():
  task_remove = (input("enter the task to you want remove:"))
  task.remove(task_remove)
  print("task removed")



def show_task():
  if len(task) == 0:
    print("No tasks available!")
  else:
    print("Your tasks are:")
    for i, t in enumerate(task, 1):
      print(f"{i}. {t}")



while True:
  print("\n""--- Todo list in python ---")
  print("1.add task")
  print("2.remove task")
  print("3.show tasks")
  print("4.exit")

  choice = int(input("enter your choice:"))
  if choice == 1:
    add_task()
  
  elif choice == 2:
    remove_task()
    
  elif choice == 3:
    show_task()

  elif choice == 4:
    print("exit form program")
    exit = input("you want to exit yes or no :")
    if exit == "no":
      continue

    else:
      print("you have exit from the progam")
      break