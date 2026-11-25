from datetime import date
from decimal import Decimal
from pathlib import Path

from expenses.report import Report
from expenses.store import Expense, Store


class TestReport:
    def store(self, tmp_path: Path) -> Store:
        store = Store(tmp_path / "e.db")
        store.add(Expense(date(2026, 3, 2), "food", Decimal("10.25")))
        store.add(Expense(date(2026, 3, 9), "food", Decimal("4.75")))
        store.add(Expense(date(2026, 3, 15), "rent", Decimal("500.00")))
        return store

    def test_totals_by_category(self, tmp_path: Path) -> None:
        assert Report(self.store(tmp_path)).by_category() == {"food": Decimal("15.00"), "rent": Decimal("500.00")}

    def test_the_total_of_a_month(self, tmp_path: Path) -> None:
        assert Report(self.store(tmp_path)).month_total(2026, 3) == Decimal("515.00")

    def test_the_first_day_of_the_next_month_is_not_in_the_month(self, tmp_path: Path) -> None:
        """Pins the upper edge: the first day of the next month is left out of the month."""
        store = self.store(tmp_path)
        store.add(Expense(date(2026, 4, 1), "food", Decimal("7.00")))
        assert Report(store).month_total(2026, 3) == Decimal("515.00")

    def test_the_last_day_of_the_month_is_in_the_month(self, tmp_path: Path) -> None:
        """Pins the inner edge: the last day of the month is counted in the month."""
        store = self.store(tmp_path)
        store.add(Expense(date(2026, 3, 31), "food", Decimal("7.00")))
        assert Report(store).month_total(2026, 3) == Decimal("522.00")

    def test_the_biggest_category(self, tmp_path: Path) -> None:
        assert Report(self.store(tmp_path)).biggest() == "rent"
