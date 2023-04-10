from functions import read_todos
import time

print('It\'s', time.strftime('%b %d, %Y %H:%M:%S'))
todos = read_todos()

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.lower()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos.append(todo.strip().capitalize() + '\n')
        print('Adding...')
    elif user_action.startswith('show') or user_action.startswith('display'):
        for index, item in enumerate(todos):
            print((index + 1), '-', item.strip('\n'))
        print('Showing...')
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            if len(todos) < int(number):
                print('Wrong number!')
            else:
                todos[int(number) - 1] = input('New to do >>> ')
                todos[int(number) - 1] = todos[int(number) - 1].capitalize().strip() + '\n'
                print('Editing...')
            for index, item in enumerate(todos):
                print((index + 1), '-', item.strip('\n'))
        except ValueError:
            print('We expect you to enter the number of task in the end.')
            continue

    elif user_action.startswith('complete'):
        try:
            num = int(user_action[9:])
            print(f'Todo "{todos[num - 1].strip()}" was removed!')
            print('Completing...')
            todos.pop(num - 1)
        except ValueError:
            print('We expect you yo enter the valid number of the task after word \'complete\'')

    elif user_action.startswith('clear'):
        file = open('todos.txt', 'w')
        file.close()
        todos.clear()
        print('Clearing...')
    elif user_action.startswith('exit') or user_action.startswith('close'):
        print('Exiting...')
        break
    else:
        print('Wrong command! ')

    with open('todos.txt', 'w') as file:
        file.writelines(todos)

print('Bye!')

