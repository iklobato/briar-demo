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

    def test_renote_changes_exactly_one_matching_expense(self, tmp_path: Path) -> None:
        store = Store(tmp_path / "e.db")
        store.add(Expense(date(2026, 3, 2), "food", Decimal("10.00"), "old"))
        store.add(Expense(date(2026, 3, 2), "food", Decimal("10.00"), "old"))
        store.add(Expense(date(2026, 3, 3), "rent", Decimal("500.00"), "march"))

        assert store.renote(date(2026, 3, 2), "food", Decimal("10.00"), "lunch") is True
        assert sorted(expense.note for expense in store.all()) == ["lunch", "march", "old"]

    def test_renote_without_a_match_returns_false(self, tmp_path: Path) -> None:
        store = Store(tmp_path / "e.db")
        store.add(Expense(date(2026, 3, 2), "food", Decimal("10.00"), "old"))

        assert store.renote(date(2026, 3, 2), "food", Decimal("11.00"), "lunch") is False
        assert [expense.note for expense in store.all()] == ["old"]
