import os

FILENAME = 'todos.txt'


def get_todo(filepath=FILENAME):
    """Read todos from file and return clean, non-empty item strings."""
    if not os.path.exists(filepath):
        with open(filepath, 'w'):
            pass
    
    with open(filepath, 'r') as file:
        todos_local = [line.strip() for line in file.readlines() if line.strip()]
    return todos_local
    
    
def write_todo(todos_arg, filepath=FILENAME):
    """Write todo items to file, storing each item on its own line."""
    if not os.path.exists(filepath):
        with open(filepath, 'w'):
            pass
    
    with open(filepath, 'w') as file:
        normalized_todos = [todo.strip() for todo in todos_arg if str(todo).strip()]
        file.writelines([f"{todo}\n" for todo in normalized_todos])
