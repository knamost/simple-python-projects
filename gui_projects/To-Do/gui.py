import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", button_color="Green")

list_box = sg.Listbox(values=functions.get_todo(), key="todos", 
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit", button_color="Blue")
complete_button = sg.Button("Complete", button_color="Blue")
exit_button = sg.Button("Exit", button_color="Red")

window = sg.Window('My To-Do App', 
                   layout=[
                       [label], 
                       [input_box, add_button], 
                       [list_box, edit_button, complete_button], 
                       [exit_button]], 
                   font=('Helvetica', 17))


while True:
    event, values = window.read()
    
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] 
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        
        
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            
            todos = functions.get_todo()
            index = todos.index(todo_to_edit)  
            todos[index] = new_todo
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        
        case "Complete":
            todo_to_remove = values['todos'][0]
            
            todos = functions.get_todo()
            todos.remove(todo_to_remove)
            
            functions.write_todo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        
        case "Exit":
            break
            
        case 'todos':
            window['todo'].update(value=values['todos'][0])
            
        case sg.WIN_CLOSED:
            break

window.close()

