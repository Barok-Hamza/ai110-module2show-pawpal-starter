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
    """A single care task for a pet (e.g. feeding, walking)."""

    title: str
    task_type: str
    date: date
    time: time
    priority: str
    pet: Pet
    completed: bool = False
    recurring: bool = False

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

    def detect_conflicts(self) -> list[Task]:
        """Return tasks that share the same date and time as another task."""
        tasks = self.get_all_tasks()
        conflicts: list[Task] = []
        for task in tasks:
            for other in tasks:
                if task is not other and task.date == other.date and task.time == other.time:
                    conflicts.append(task)
                    break
        return conflicts

    def generate_recurring_tasks(self) -> list[Task]:
        """Create the next daily occurrence for each recurring task."""
        new_tasks: list[Task] = []
        for task in self.get_all_tasks():
            if task.recurring:
                next_task = Task(
                    title=task.title,
                    task_type=task.task_type,
                    date=task.date + timedelta(days=1),
                    time=task.time,
                    priority=task.priority,
                    pet=task.pet,
                    completed=False,
                    recurring=True,
                )
                task.pet.add_task(next_task)
                new_tasks.append(next_task)
        return new_tasks
