"""PawPal+ demo script.

Creates an owner with a few pets and tasks, then prints
today's schedule in chronological order.
"""

from datetime import date, time

from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    """Build a small example and print today's schedule."""
    # 1. Create one owner.
    owner = Owner("Barok", "barok@example.com")

    # 2. Create two pets and add them to the owner.
    rex = Pet("Rex", "dog", 3, owner)
    mittens = Pet("Mittens", "cat", 2, owner)
    owner.add_pet(rex)
    owner.add_pet(mittens)

    # 3. Create three tasks for today at different times.
    today = date.today()
    breakfast = Task("Morning feeding", "food", today, time(8, 0), "high", rex)
    litter = Task("Clean litter box", "cleaning", today, time(12, 30), "medium", mittens)
    walk = Task("Evening walk", "exercise", today, time(18, 0), "high", rex)

    # 4. Assign the tasks to the correct pets through the scheduler.
    scheduler = Scheduler(owner)
    scheduler.add_task(breakfast)
    scheduler.add_task(litter)
    scheduler.add_task(walk)

    # 5. Print today's schedule in chronological order.
    print("Today's Schedule")
    print("=" * 60)

    today_tasks = scheduler.get_today_tasks()
    today_tasks.sort(key=lambda task: task.time)

    for task in today_tasks:
        status = "Done" if task.completed else "Not done"
        print(
            f"{task.time.strftime('%H:%M')} | "
            f"{task.pet.name} | "
            f"{task.title} | "
            f"{task.task_type} | "
            f"priority: {task.priority} | "
            f"{status}"
        )


if __name__ == "__main__":
    main()
