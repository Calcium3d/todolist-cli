import pickle
todos = pickle.load(open("names.dat", "rb"))

print(
    "What do you want to do? \n \n For seeing lists - display \n For adding todos - add \n for removing todos - remove \n to exit program - exit")

while True:
    enter = input("Enter choice: ")
    print("\n")

    if enter == "display":
        for todo in todos:
            print(str(todos.index(todo) + 1) + ". " + todo)
            
    if enter == "add":
        a = input("Enter the todo: ")
        todos.append(a)
        pickle.dump(todos, open("names.dat", "wb"))

    if enter == "remove":
        b = int(input("Enter the no of the todo: "))
        todos.pop(b - 1)
        pickle.dump(todos, open("names.dat", "wb"))

    if enter == "exit":
        print("Stopping program")
        pickle.dump(todos, open("names.dat", "wb"))
        break

