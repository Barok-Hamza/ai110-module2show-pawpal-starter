"""Beginner-friendly tests for PawPal+."""

import os
import sys
from datetime import date, time, timedelta

# Make sure the project root is importable when running these tests.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion():
    """Calling mark_complete() should set completed to True."""
    owner = Owner("Barok", "barok@example.com")
    pet = Pet("Rex", "dog", 3, owner)
    task = Task("Morning feeding", "food", date.today(), time(8, 0), "high", pet)

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    """Adding a task to a pet should increase its task count by 1."""
    owner = Owner("Barok", "barok@example.com")
    pet = Pet("Mittens", "cat", 2, owner)

    initial_count = len(pet.get_tasks())
    task = Task("Clean litter box", "cleaning", date.today(), time(12, 30), "medium", pet)
    pet.add_task(task)

    assert len(pet.get_tasks()) == initial_count + 1


def test_sort_by_time():
    """sort_by_time() should return tasks in chronological order."""
    owner = Owner("Barok", "barok@example.com")
    pet = Pet("Rex", "dog", 3, owner)
    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    today = date.today()
    # Add three tasks in an unsorted (out-of-order) order.
    evening = Task("Evening walk", "exercise", today, time(18, 0), "high", pet)
    morning = Task("Morning feeding", "food", today, time(8, 0), "high", pet)
    noon = Task("Midday play", "exercise", today, time(12, 0), "low", pet)
    scheduler.add_task(evening)
    scheduler.add_task(morning)
    scheduler.add_task(noon)

    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks == [morning, noon, evening]


def test_daily_recurrence():
    """Completing a daily task should create the next day's occurrence."""
    owner = Owner("Barok", "barok@example.com")
    pet = Pet("Mittens", "cat", 2, owner)
    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    today = date.today()
    task = Task(
        "Clean litter box", "cleaning", today, time(8, 0), "medium", pet,
        frequency="daily",
    )
    scheduler.add_task(task)

    new_task = scheduler.mark_task_complete(task)

    assert task.completed is True
    assert new_task is not None
    assert new_task.date == today + timedelta(days=1)
    assert new_task.completed is False
    assert new_task.frequency == "daily"


def test_conflict_detection():
    """Two tasks at the same date and time should produce one warning."""
    owner = Owner("Barok", "barok@example.com")
    pet = Pet("Rex", "dog", 3, owner)
    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    today = date.today()
    feeding = Task("Morning feeding", "food", today, time(8, 0), "high", pet)
    walk = Task("Morning walk", "exercise", today, time(8, 0), "high", pet)
    scheduler.add_task(feeding)
    scheduler.add_task(walk)

    warnings = scheduler.detect_conflicts()

    assert len(warnings) == 1
    assert "Morning feeding" in warnings[0]
    assert "Morning walk" in warnings[0]


def test_pet_starts_with_no_tasks():
    """A brand new pet should start with an empty task list."""
    owner = Owner("Barok", "barok@example.com")
    pet = Pet("Buddy", "dog", 1, owner)

    assert pet.get_tasks() == []
