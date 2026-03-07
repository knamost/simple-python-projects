import functions
import FreeSimpleGUI as sg
import time

def read_todos_clean():
    """Return todos without trailing newlines for GUI display and matching."""
    return [todo.strip() for todo in functions.get_todo() if todo.strip()]


def write_todos_clean(todos):
    """Persist GUI todos back to file with newline delimiters."""
    functions.write_todo([f"{todo}\n" for todo in todos])

sg.theme("DarkPurple4")

clock = sg.Text('', key='current_time')

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(image_source="./images/add.png", mouseover_colors="Green", key="Add")

list_box = sg.Listbox(values=read_todos_clean(), key="todos", 
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit", button_color="Blue")
complete_button = sg.Button(size=10, image_source="./images/complete.png", key="Complete")
exit_button = sg.Button("Exit", button_color="Red")

window = sg.Window('My To-Do App', 
                   layout=[
                       [clock],
                       [label], 
                       [input_box, add_button], 
                       [list_box, edit_button, complete_button], 
                       [exit_button]], 
                   font=('Helvetica', 17))


while True:
    event, values = window.read(timeout=1000)
    window['current_time'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    
    match event:
        case "Add":
            todos = read_todos_clean()
            new_todo = values['todo'].strip()

            if not new_todo:
                sg.popup("Please enter a non-empty to-do item", font=('Helvetica', 17))
                continue

            todos.append(new_todo)
            write_todos_clean(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        
        
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].strip()

                if not new_todo:
                    sg.popup("Edited to-do cannot be empty", font=('Helvetica', 17))
                    continue
                
                todos = read_todos_clean()
                index = todos.index(todo_to_edit)  
                todos[index] = new_todo
                write_todos_clean(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 17))
            except ValueError:
                sg.popup("Selected item no longer exists. Please try again.", font=('Helvetica', 17))
        
        case "Complete":
            try:
                todo_to_remove = values['todos'][0]
                
                todos = read_todos_clean()
                todos.remove(todo_to_remove)
                
                write_todos_clean(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 17))
                
        
        case "Exit":
            break
            
        case 'todos':
            try:
                window['todo'].update(value=values['todos'][0])
            except:
                pass # item dont exist
        case sg.WIN_CLOSED:
            break

window.close()

