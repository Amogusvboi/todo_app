def read_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos