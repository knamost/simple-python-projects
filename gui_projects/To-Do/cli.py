from functions import get_todo, write_todo
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    """Write a to-do items in the text files"""
    # Get user input and strip space character from it
    user_actions = input("Type add or show or edit or complete or exit: ").strip()

    if user_actions.startswith("add"):
        todo = user_actions[4:].strip()

        if not todo:
            print("Todo cannot be empty")
            continue
        
        todos = get_todo()
        todos.append(todo)
        
        write_todo(todos)
        
    elif user_actions.startswith("show"):
        todos = get_todo()
        for index, item in enumerate(todos):
            print(f"{index+1}-{item}")
                
    elif user_actions.startswith("edit"):
        try:
            number = int(user_actions[5:])                
            number = number - 1
            
            todos = get_todo()
            print(f"Item to edit: {todos[number]}")
            new_todo = input("Enter new todo: ").strip()

            if not new_todo:
                print("Todo cannot be empty")
                continue

            todos[number] = new_todo
            
            write_todo(todos)
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There's no item with that number..")
            continue
        
        
    elif user_actions.startswith("complete"):
        try:
            number = int(user_actions[9:])
            if number > 0:
                
                todos = get_todo()
                    
                todo_to_remove = todos[number-1]
                todos.pop(number-1)
                
                write_todo(todos)
                print(f"Todo {todo_to_remove} was removed from list..")
        except IndexError:
            print("There's no item with that number..")
        
        
    elif user_actions.startswith("exit"):
        break
    else:
        print("Invalid options")


def main():
    print("thanks for using our todo program")

if __name__ == "__main__":
    main()
