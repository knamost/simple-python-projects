FILENAME = 'todos_item.txt'

def get_todo(filepath=FILENAME):
    """Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local    
    

def write_todo(todos_arg, filepath=FILENAME ):
    """ Write the to-do items in list in the text file."""
    with open(filepath, 'w') as file:
        todo = file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todo())