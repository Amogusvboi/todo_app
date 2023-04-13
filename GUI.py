import new_functions
import PySimpleGUI as sg
import time

sg.theme('Black')

clock = sg.Text('',key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=new_functions.read_todos(),key=('todos'),
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit', key=('Edit'))
complete_button = sg.Button('Complete', key=('Complete'))
close_button = sg.Button('Ready')

window = sg.Window('To-Do Application',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [complete_button, close_button, clock]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(time.strftime('%H:%M:%S'))
    print(event)
    print(values)
    print('Clothing...')
    match event:
        case 'Add':
            todos = new_functions.read_todos()
            todos.append(values['todo'] + '\n')
            new_functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = new_functions.read_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                new_functions.write_todos(todos)
                window['todos'].update(values=todos)
            except:
                sg.popup('Please select an item first!', font=('Helvetiva', 12))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todos = new_functions.read_todos()
                todos.remove(values['todos'][0])
                new_functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except:
                sg.popup('Please select an item first!', font=('Helvetica', 12))
        case sg.WIN_CLOSED:
            break
        case 'Ready':
            break
window.close()