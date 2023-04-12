import new_functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')
close_button = sg.Button('Ready')


window = sg.Window('To-Do Application',
                   layout=[[label], [input_box, add_button],
                   [close_button]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print('Clothing...')
    match event:
        case 'Add':
            todos = new_functions.read_todos()
            todos.append(values['todo'] + '\n')
            new_functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
        case 'Ready':
            break
window.close()