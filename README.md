# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## Features

PawPal+ provides:

- **Pet and owner management** — one owner can keep a list of pets, and each pet keeps its own list of care tasks.
- **Task scheduling** — create tasks with a title, type, date, time, and priority, and attach them to the right pet.
- **Sorting by date and time** — `Scheduler.sort_tasks()` orders tasks by date then time; `Scheduler.sort_by_time()` orders any list of tasks by time.
- **Filtering by pet and completion status** — `Scheduler.filter_tasks()` narrows tasks down by pet name, completion status, or both.
- **Exact-time conflict warnings** — `Scheduler.detect_conflicts()` returns readable warnings for tasks sharing the same date and time, naming both tasks and their pets.
- **Daily and weekly recurring tasks** — a task's `frequency` can be `"none"`, `"daily"`, or `"weekly"`; completing a recurring task through `Scheduler.mark_task_complete()` automatically creates the next occurrence.
- **Streamlit session-state persistence** — the app keeps one `Owner` and one `Scheduler` in `st.session_state`, so pets and tasks survive across reruns.
- **Automated pytest verification** — a beginner-friendly test suite checks completion, task counts, sorting, recurrence, conflict detection, and the empty-task edge case.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Running `python main.py` demonstrates sorting, filtering, conflict detection, and recurrence.
See the full output under [Demo Walkthrough → CLI demo output](#cli-demo-output).

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_tasks()`, `Scheduler.sort_by_time()` | Orders tasks by date+time, or any task list by time |
| Filtering | `Scheduler.filter_tasks()` | Filter by pet name, completion status, or both |
| Conflict handling | `Scheduler.detect_conflicts()` | Warns about tasks at the exact same date and time |
| Recurring tasks | `Scheduler.mark_task_complete()`, `Scheduler.generate_recurring_tasks()` | Creates the next daily or weekly occurrence |

## Demo Walkthrough

Follow these steps in the Streamlit app (`streamlit run app.py`):

1. **Add a pet** — in the *Add Pet* form, enter a name, species, and age, then click **Add pet**. The pet appears in *Your pets*.
2. **Schedule a task** — in the *Schedule Task* form, pick the pet, enter a title and type, choose a date, time, and priority.
3. **Select recurrence** — use the *Repeat* dropdown to choose `none`, `daily`, or `weekly`, then click **Add task**.
4. **View sorted tasks** — the *Scheduled tasks* table lists every task ordered by time, including its repeat frequency and completion status.
5. **Filter tasks** — use *Filter by pet* and *Filter by status* to narrow the table down to a single pet and/or only incomplete or completed tasks.
6. **See conflict warnings** — if two tasks share the exact same date and time, a warning appears; otherwise you'll see a "No scheduling conflicts" confirmation.
7. **Generate today's schedule** — click **Generate schedule** to see today's tasks listed in chronological order.

### Example workflow

> **add a pet → schedule tasks → review conflicts → generate the schedule**

Add "Rex" the dog, schedule a morning feeding and an evening walk, notice the conflict warning when two tasks land at the same time, then generate the schedule to see the day laid out in order.

### CLI demo output

Running the command-line demo (`python main.py`) prints the same scheduling features:

```text
Tasks sorted by time
----------------------------------------
08:00 | Rex | Morning feeding
08:00 | Mittens | Clean litter box
12:00 | Mittens | Vet visit
18:00 | Rex | Evening walk

Tasks for Rex
----------------------------------------
18:00 | Evening walk
08:00 | Morning feeding

Incomplete tasks
----------------------------------------
Rex | Evening walk
Rex | Morning feeding
Mittens | Clean litter box

Conflict warnings
----------------------------------------
Conflict on 2026-07-11 at 08:00: 'Morning feeding' (Rex) and 'Clean litter box' (Mittens)

New recurring task
----------------------------------------
Created: Clean litter box for Mittens on 2026-07-12 at 08:00
```

## Testing PawPal+

Run the automated tests with:

```bash
python -m pytest
```

The test suite verifies:

- Completing a task changes its status
- Adding a task increases a pet's task count
- Tasks are sorted chronologically
- Daily recurring tasks create the next day's occurrence
- Scheduling conflicts are detected
- New pets begin with no tasks

### Successful Test Run

```text
Paste your successful pytest output here.
```

### Confidence Level

⭐⭐⭐⭐⭐ 5/5

All automated tests pass, including the main scheduling features and important edge cases.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
