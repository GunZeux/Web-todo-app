import streamlit as st
import modules.functions as func


todos = func.get_todo()


def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local+"\n")
    func.write_todo(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This increases your productivity")

for todo in todos:
    check = st.checkbox(todo, key=todo)
    if check:
        todos.remove(todo)
        func.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ",
              placeholder="Add a Todo....", key="new_todo",
              on_change=add_todo)
