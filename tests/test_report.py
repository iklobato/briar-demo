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

    def test_totals_by_month(self, tmp_path: Path) -> None:
        store = self.store(tmp_path)
        store.add(Expense(date(2026, 4, 1), "food", Decimal("7.50")))
        store.add(Expense(date(2026, 4, 30), "rent", Decimal("500.00")))
        totals = Report(store).by_month()
        assert totals == {"2026-03": Decimal("515.00"), "2026-04": Decimal("507.50")}
        assert list(totals) == ["2026-03", "2026-04"]

    def test_the_biggest_category(self, tmp_path: Path) -> None:
        assert Report(self.store(tmp_path)).biggest() == "rent"
