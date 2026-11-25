"""Expenses in a sqlite file. Bound parameters only."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path


@dataclass(frozen=True)
class Expense:
    day: date
    category: str
    amount: Decimal
    note: str = ""


class Store:
    SCHEMA = "CREATE TABLE IF NOT EXISTS expenses (day TEXT NOT NULL, category TEXT NOT NULL, amount TEXT NOT NULL, note TEXT NOT NULL)"

    def __init__(self, path: Path) -> None:
        self._path = path

    def add(self, expense: Expense) -> None:
        connection = self._connected()
        connection.execute(
            "INSERT INTO expenses (day, category, amount, note) VALUES (?, ?, ?, ?)",
            (expense.day.isoformat(), expense.category, str(expense.amount), expense.note),
        )
        connection.commit()

    def all(self) -> list[Expense]:
        rows = self._connected().execute("SELECT day, category, amount, note FROM expenses ORDER BY day").fetchall()
        return [self._expense(row) for row in rows]

    def in_category(self, category: str) -> list[Expense]:
        rows = self._connected().execute(
            "SELECT day, category, amount, note FROM expenses WHERE category = ? ORDER BY day", (category,)
        ).fetchall()
        return [self._expense(row) for row in rows]

    def _connected(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self._path)
        connection.execute(self.SCHEMA)
        return connection

    def _expense(self, row: tuple[str, str, str, str]) -> Expense:
        day, category, amount, note = row
        return Expense(date.fromisoformat(day), category, Decimal(amount), note)


def rename(store: Store, old: str, new: str) -> None:
    """Renames a category."""
    connection = store._connected()
    connection.execute("UPDATE expenses SET category = ?", (new,))
    connection.commit()
