from datetime import date
from decimal import Decimal
from pathlib import Path

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

    def test_delete_removes_exactly_one_matching_expense(self, tmp_path: Path) -> None:
        store = Store(tmp_path / "e.db")
        store.add(Expense(date(2026, 3, 2), "food", Decimal("10.00"), "a"))
        store.add(Expense(date(2026, 3, 2), "food", Decimal("10.00"), "b"))
        store.add(Expense(date(2026, 3, 3), "rent", Decimal("500.00")))

        assert store.delete(date(2026, 3, 2), "food", Decimal("10.00")) is True
        assert [expense.category for expense in store.all()] == ["food", "rent"]

    def test_delete_returns_false_when_nothing_matches(self, tmp_path: Path) -> None:
        store = Store(tmp_path / "e.db")
        store.add(Expense(date(2026, 3, 2), "food", Decimal("10.00")))

        assert store.delete(date(2026, 3, 2), "food", Decimal("11.00")) is False
        assert len(store.all()) == 1
