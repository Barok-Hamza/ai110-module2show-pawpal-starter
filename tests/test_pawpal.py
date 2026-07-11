"""Beginner-friendly tests for PawPal+."""

import os
import sys
from datetime import date, time

# Make sure the project root is importable when running these tests.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pawpal_system import Owner, Pet, Task


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
