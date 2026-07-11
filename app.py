import streamlit as st
from datetime import date, time

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

# --- Set up shared data that survives Streamlit reruns ---------------------
# Create one Owner and one Scheduler and keep them in session_state so that
# adding a pet or a task does not get erased every time the page reruns.
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan", "jordan@example.com")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(st.session_state.owner)

owner = st.session_state.owner
scheduler = st.session_state.scheduler

st.divider()

# --- Add Pet ---------------------------------------------------------------
st.subheader("Add Pet")

with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name", value="Mochi")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    age = st.number_input("Age", min_value=0, max_value=100, value=1)
    add_pet_submitted = st.form_submit_button("Add pet")

    if add_pet_submitted:
        # Create a Pet from the form values and add it to the owner.
        new_pet = Pet(pet_name, species, int(age), owner)
        owner.add_pet(new_pet)
        st.success(f"Added {new_pet.name} the {new_pet.species}!")

# Show the current list of pets from the Owner object.
if owner.get_pets():
    st.write("Your pets:")
    for pet in owner.get_pets():
        st.write(f"- {pet.name} ({pet.species}, age {pet.age})")
else:
    st.info("No pets yet. Add one above.")

st.divider()

# --- Schedule Task ---------------------------------------------------------
st.subheader("Schedule Task")

if owner.get_pets():
    with st.form("schedule_task_form"):
        pet_names = [pet.name for pet in owner.get_pets()]
        selected_pet_name = st.selectbox("Pet", pet_names)
        task_title = st.text_input("Task title", value="Morning walk")
        task_type = st.text_input("Task type", value="exercise")
        task_date = st.date_input("Date", value=date.today())
        task_time = st.time_input("Time", value=time(8, 0))
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
        recurring = st.checkbox("Recurring daily")
        add_task_submitted = st.form_submit_button("Add task")

        if add_task_submitted:
            # Find the Pet object the user picked in the dropdown.
            selected_pet = None
            for pet in owner.get_pets():
                if pet.name == selected_pet_name:
                    selected_pet = pet
                    break

            # Create the Task and add it through the scheduler.
            task = Task(
                task_title,
                task_type,
                task_date,
                task_time,
                priority,
                selected_pet,
                recurring=recurring,
            )
            scheduler.add_task(task)
            st.success(f"Scheduled '{task.title}' for {selected_pet.name}!")
else:
    st.info("Add a pet first before scheduling tasks.")

# Show every task across all of the owner's pets.
all_tasks = scheduler.get_all_tasks()
if all_tasks:
    st.write("All scheduled tasks:")
    task_rows = [
        {
            "pet": task.pet.name,
            "title": task.title,
            "type": task.task_type,
            "date": str(task.date),
            "time": task.time.strftime("%H:%M"),
            "priority": task.priority,
            "done": task.completed,
        }
        for task in all_tasks
    ]
    st.table(task_rows)
else:
    st.info("No tasks yet. Schedule one above.")

st.divider()

# --- Build Schedule --------------------------------------------------------
st.subheader("Build Schedule")
st.caption("Show today's tasks in order using your Scheduler.")

if st.button("Generate schedule"):
    today_tasks = scheduler.get_today_tasks()
    today_tasks.sort(key=lambda task: task.time)

    if today_tasks:
        st.write("Today's Schedule")
        for task in today_tasks:
            status = "Done" if task.completed else "Not done"
            st.write(
                f"{task.time.strftime('%H:%M')} — {task.pet.name}: "
                f"{task.title} ({task.task_type}, priority: {task.priority}) — {status}"
            )
    else:
        st.info("No tasks are due today.")
