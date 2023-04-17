import streamlit as st
import new_functions as nf

todos = nf.read_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    nf.write_todos(todos)

st.title('My to-do App')

for item in todos:
    st.checkbox(item)

st.text_input(label='', placeholder='Add new todo...', on_change=add_todo, key='new_todo')

st.session_state