FILEPATH = 'todos.txt'

def read_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file:
        local_todos = file.readlines()
    return local_todos

def write_todos(todos, filepath = FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos)

if __name__ == '__main__':
    print('We are testing the new_functions code now')