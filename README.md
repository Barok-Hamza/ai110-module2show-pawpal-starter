# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

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

```text
Today's Schedule
============================================================
08:00 | Rex | Morning feeding | food | priority: high | Not done
12:30 | Mittens | Clean litter box | cleaning | priority: medium | Not done
18:00 | Rex | Evening walk | exercise | priority: high | Not done
```

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

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->



## Smarter Scheduling

- Sorting: `Scheduler.sort_by_time()` sorts tasks by time.
- Filtering: `Scheduler.filter_tasks()` filters tasks by pet or completion status.
- Conflict Detection: `Scheduler.detect_conflicts()` reports tasks scheduled at the same date and time.
- Recurring Tasks: `Scheduler.mark_task_complete()` automatically creates the next daily or weekly task.


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
