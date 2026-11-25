import sqlite3
from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest

from expenses.store import Expense, Store


class TestStore:
    def test_what_is_added_comes_back_in_day_order(self, tmp_path: Path) -> None:
        store = Store(tmp_path / "e.db")
        store.add(Expense(date(2026, 3, 2), "food", Decimal("10.00")))
        store.add(Expense(date(2026, 3, 1), "rent", Decimal("500.00"), "march"))

        assert [expense.category for expense in store.all()] == ["rent", "food"]

    def test_a_category_lists_only_its_expenses(self, tmp_path: Path) -> None:
        store = Store(tmp_path / "e.db")
        store.add(Expense(date(2026, 3, 2), "food", Decimal("10.00")))
        store.add(Expense(date(2026, 3, 3), "rent", Decimal("500.00")))

        assert [expense.amount for expense in store.in_category("food")] == [Decimal("10.00")]

    def test_every_connection_is_closed_when_the_call_ends(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        opened: list[sqlite3.Connection] = []
        connect = sqlite3.connect

        def recording_connect(*args: object, **kwargs: object) -> sqlite3.Connection:
            connection = connect(*args, **kwargs)
            opened.append(connection)
            return connection

        monkeypatch.setattr(sqlite3, "connect", recording_connect)
        store = Store(tmp_path / "e.db")
        store.add(Expense(date(2026, 3, 2), "food", Decimal("10.00")))
        store.all()
        store.in_category("food")

        assert len(opened) == 3
        for connection in opened:
            with pytest.raises(sqlite3.ProgrammingError):
                connection.execute("SELECT 1")
