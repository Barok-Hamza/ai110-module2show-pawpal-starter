"""PawPal+ demo script.

Shows off the Phase 4 scheduling features: sorting, filtering,
conflict detection, and recurring tasks.
"""

from datetime import date, time

from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    """Build an example schedule and print the Phase 4 features."""
    # 1. Create one owner and two pets.
    owner = Owner("Barok", "barok@example.com")
    rex = Pet("Rex", "dog", 3, owner)
    mittens = Pet("Mittens", "cat", 2, owner)
    owner.add_pet(rex)
    owner.add_pet(mittens)

    scheduler = Scheduler(owner)

    today = date.today()

    # 2. Create tasks in an intentionally unsorted (out-of-order) list.
    #    - two pets are represented
    #    - some tasks are completed, some are not
    #    - one task recurs daily
    #    - two tasks share the exact same date and time (a conflict)
    evening_walk = Task("Evening walk", "exercise", today, time(18, 0), "high", rex)
    litter_box = Task(
        "Clean litter box", "cleaning", today, time(8, 0), "medium", mittens,
        frequency="daily",
    )
    morning_feeding = Task("Morning feeding", "food", today, time(8, 0), "high", rex)
    vet_visit = Task("Vet visit", "health", today, time(12, 0), "low", mittens)

    # Mark one task as already completed.
    vet_visit.mark_complete()

    # Add them through the scheduler (note the unsorted order).
    for task in (evening_walk, litter_box, morning_feeding, vet_visit):
        scheduler.add_task(task)

    # 3. Tasks sorted by time.
    print("Tasks sorted by time")
    print("-" * 40)
    for task in scheduler.sort_by_time():
        print(f"{task.time.strftime('%H:%M')} | {task.pet.name} | {task.title}")
    print()

    # 4. Tasks filtered by pet.
    print("Tasks for Rex")
    print("-" * 40)
    for task in scheduler.filter_tasks(pet_name="Rex"):
        print(f"{task.time.strftime('%H:%M')} | {task.title}")
    print()

    # 5. Incomplete tasks.
    print("Incomplete tasks")
    print("-" * 40)
    for task in scheduler.filter_tasks(completed=False):
        print(f"{task.pet.name} | {task.title}")
    print()

    # 6. Conflict warnings.
    print("Conflict warnings")
    print("-" * 40)
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for warning in conflicts:
            print(warning)
    else:
        print("No conflicts found.")
    print()

    # 7. Mark the recurring task complete and show the new occurrence.
    print("New recurring task")
    print("-" * 40)
    new_task = scheduler.mark_task_complete(litter_box)
    if new_task is not None:
        print(
            f"Created: {new_task.title} for {new_task.pet.name} "
            f"on {new_task.date} at {new_task.time.strftime('%H:%M')}"
        )
    else:
        print("No new recurring task was created.")


if __name__ == "__main__":
    main()
