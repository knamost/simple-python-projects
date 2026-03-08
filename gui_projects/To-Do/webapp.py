import streamlit as st
import functions


def add_todo():
    """Add a new todo item and save it."""
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    functions.write_todo(todos)
    

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

todos = functions.get_todo()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo", on_change=add_todo, key="new_todo")
