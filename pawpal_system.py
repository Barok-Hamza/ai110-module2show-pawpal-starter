"""PawPal+ - A beginner-friendly pet care management app.

This module defines the four main classes for PawPal+:
Owner, Pet, Task, and Scheduler.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, time, timedelta


class Owner:
    """A person who owns one or more pets."""

    def __init__(self, name: str, email: str) -> None:
        self.name: str = name
        self.email: str = email
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner if it is not already present."""
        if pet not in self.pets:
            self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner if it is present."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pets(self) -> list[Pet]:
        """Return the list of pets belonging to this owner."""
        return self.pets

    def get_all_tasks(self) -> list[Task]:
        """Return every task from all of this owner's pets."""
        all_tasks: list[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


@dataclass
class Pet:
    """An animal cared for by an owner."""

    name: str
    species: str
    age: int
    owner: Owner
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet if it is not already present."""
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet if it is present."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self) -> list[Task]:
        """Return the list of tasks for this pet."""
        return self.tasks


@dataclass
class Task:
    """A single care task for a pet (e.g. feeding, walking).

    frequency controls recurrence: "none", "daily", or "weekly".
    """

    title: str
    task_type: str
    date: date
    time: time
    priority: str
    pet: Pet
    completed: bool = False
    frequency: str = "none"

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def update_priority(self, priority: str) -> None:
        """Change the priority level of this task."""
        self.priority = priority

    def is_due_today(self) -> bool:
        """Return True if this task's date is today."""
        return self.date == date.today()


class Scheduler:
    """Manages and organizes tasks across all of an owner's pets."""

    def __init__(self, owner: Owner) -> None:
        self.owner: Owner = owner

    def get_all_tasks(self) -> list[Task]:
        """Return every task from all of the owner's pets."""
        return self.owner.get_all_tasks()

    def add_task(self, task: Task) -> None:
        """Add a task to its associated pet."""
        task.pet.add_task(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from its associated pet."""
        task.pet.remove_task(task)

    def get_today_tasks(self) -> list[Task]:
        """Return all tasks that are due today."""
        return [task for task in self.get_all_tasks() if task.is_due_today()]

    def sort_tasks(self) -> list[Task]:
        """Return all tasks sorted by date and then time."""
        return sorted(self.get_all_tasks(), key=lambda task: (task.date, task.time))

    def sort_by_time(self, tasks: list[Task] | None = None) -> list[Task]:
        """Return tasks sorted by time; uses all owner tasks when none are given."""
        if tasks is None:
            tasks = self.get_all_tasks()
        return sorted(tasks, key=lambda task: task.time)

    def filter_tasks(
        self, pet_name: str | None = None, completed: bool | None = None
    ) -> list[Task]:
        """Return tasks filtered by pet name and/or completion status."""
        tasks = self.get_all_tasks()
        if pet_name is not None:
            tasks = [task for task in tasks if task.pet.name == pet_name]
        if completed is not None:
            tasks = [task for task in tasks if task.completed == completed]
        return tasks

    def detect_conflicts(self) -> list[str]:
        """Return readable warnings for tasks sharing the same date and time."""
        tasks = self.get_all_tasks()
        warnings: list[str] = []
        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                first = tasks[i]
                second = tasks[j]
                if first.date == second.date and first.time == second.time:
                    warnings.append(
                        f"Conflict on {first.date} at {first.time.strftime('%H:%M')}: "
                        f"'{first.title}' ({first.pet.name}) and "
                        f"'{second.title}' ({second.pet.name})"
                    )
        return warnings

    def _next_date(self, task: Task) -> date | None:
        """Return the next date for a recurring task, or None if it does not recur."""
        if task.frequency == "daily":
            return task.date + timedelta(days=1)
        if task.frequency == "weekly":
            return task.date + timedelta(weeks=1)
        return None

    def _make_next_occurrence(self, task: Task, next_date: date) -> Task:
        """Build the next occurrence of a recurring task on the given date."""
        return Task(
            title=task.title,
            task_type=task.task_type,
            date=next_date,
            time=task.time,
            priority=task.priority,
            pet=task.pet,
            completed=False,
            frequency=task.frequency,
        )

    def _occurrence_exists(self, task: Task, next_date: date) -> bool:
        """Return True if the pet already has this task on the given date and time."""
        for other in task.pet.get_tasks():
            if (
                other.title == task.title
                and other.date == next_date
                and other.time == task.time
            ):
                return True
        return False

    def mark_task_complete(self, task: Task) -> Task | None:
        """Mark a task complete and add its next occurrence if it recurs and is new."""
        task.mark_complete()
        next_date = self._next_date(task)
        if next_date is None:
            return None
        if self._occurrence_exists(task, next_date):
            return None
        next_task = self._make_next_occurrence(task, next_date)
        task.pet.add_task(next_task)
        return next_task

    def generate_recurring_tasks(self) -> list[Task]:
        """Create the next occurrence for each recurring task, skipping duplicates."""
        new_tasks: list[Task] = []
        for task in list(self.get_all_tasks()):
            next_date = self._next_date(task)
            if next_date is None:
                continue
            if self._occurrence_exists(task, next_date):
                continue
            next_task = self._make_next_occurrence(task, next_date)
            task.pet.add_task(next_task)
            new_tasks.append(next_task)
        return new_tasks
