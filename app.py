import streamlit as st

st.title("To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

def add_task():
    task = st.session_state.new_task.strip()
    if task:
        st.session_state.tasks.append({"text": task, "done": False})
    st.session_state.new_task = ""

st.text_input("Add a task", key="new_task", on_change=add_task)

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.9, 0.1])
    with col1:
        task["done"] = st.checkbox(
            task["text"], value=task["done"], key=f"task_{i}"
        )
    with col2:
        if st.button("🗑️", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()

remaining = sum(1 for t in st.session_state.tasks if not t["done"])
st.caption(f"{remaining} task(s) remaining")
