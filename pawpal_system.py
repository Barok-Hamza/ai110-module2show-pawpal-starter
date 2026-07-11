"""PawPal+ - A beginner-friendly pet care management app.

This module defines the four main classes for PawPal+:
Owner, Pet, Task, and Scheduler.

The method bodies are left as skeletons for now. The real
scheduling logic will be added later.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, time


class Owner:
    """A person who owns one or more pets."""

    def __init__(self, name: str, email: str) -> None:
        self.name: str = name
        self.email: str = email
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's list of pets."""
        pass

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner's list of pets."""
        pass

    def get_pets(self) -> list[Pet]:
        """Return the list of pets belonging to this owner."""
        return self.pets


@dataclass
class Pet:
    """An animal cared for by an owner."""

    name: str
    species: str
    age: int
    owner: Owner
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a care task for this pet."""
        pass

    def remove_task(self, task: Task) -> None:
        """Remove a care task from this pet."""
        pass

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
        pass

    def update_priority(self, priority: str) -> None:
        """Change the priority level of this task."""
        pass

    def is_due_today(self) -> bool:
        """Return True if this task is due today."""
        return False


class Scheduler:
    """Manages and organizes tasks across all pets."""

    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the scheduler."""
        pass

    def remove_task(self, task: Task) -> None:
        """Remove a task from the scheduler."""
        pass

    def get_today_tasks(self) -> list[Task]:
        """Return all tasks that are due today."""
        return []

    def sort_tasks(self) -> list[Task]:
        """Return the tasks sorted (e.g. by date, time, or priority)."""
        return []

    def detect_conflicts(self) -> list:
        """Return any tasks that conflict with each other."""
        return []

    def generate_recurring_tasks(self) -> list[Task]:
        """Create the next occurrences for recurring tasks."""
        return []
