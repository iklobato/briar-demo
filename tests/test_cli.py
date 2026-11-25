from datetime import date
from decimal import Decimal
from pathlib import Path

from expenses.cli import Cli
from expenses.store import Expense, Store


class TestCliDelete:
    def test_delete_removes_a_matching_expense_and_exits_0(self, tmp_path: Path) -> None:
        db = tmp_path / "e.db"
        Store(db).add(Expense(date(2026, 3, 2), "food", Decimal("12.50")))

        assert Cli().run(["--db", str(db), "delete", "2026-03-02", "food", "12.5"]) == 0
        assert Store(db).all() == []

    def test_delete_exits_1_when_nothing_matches(self, tmp_path: Path) -> None:
        db = tmp_path / "e.db"
        Store(db).add(Expense(date(2026, 3, 2), "food", Decimal("12.50")))

        assert Cli().run(["--db", str(db), "delete", "2026-03-02", "rent", "12.50"]) == 1
        assert len(Store(db).all()) == 1
