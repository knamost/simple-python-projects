import os

FILENAME = 'todos.txt'

def ensure_file_exists(filepath=FILENAME):
    """Create the todo file (and parent directory) when it does not exist."""
    parent_dir = os.path.dirname(filepath)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    if not os.path.exists(filepath):
        with open(filepath, 'w'):
            pass

def get_todo(filepath=FILENAME):
    """Read todos from file and return clean, non-empty item strings."""
    ensure_file_exists(filepath)
    with open(filepath, 'r') as file:
        todos_local = [line.strip() for line in file.readlines() if line.strip()]
    return todos_local
    
    
def write_todo(todos_arg, filepath=FILENAME ):
    """Write todo items to file, storing each item on its own line."""
    ensure_file_exists(filepath)
    with open(filepath, 'w') as file:
        normalized_todos = [todo.strip() for todo in todos_arg if str(todo).strip()]
        file.writelines([f"{todo}\n" for todo in normalized_todos])
