import streamlit as st
import new_functions as nf

todos = nf.read_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    nf.write_todos(todos)

st.title('My to-do App')

index = 0
for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        nf.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add new todo...', on_change=add_todo, key='new_todo')