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

    def test_the_biggest_category(self, tmp_path: Path) -> None:
        assert Report(self.store(tmp_path)).biggest() == "rent"

    def test_over_budget_returns_categories_above_their_limit(self, tmp_path: Path) -> None:
        limits = {"rent": Decimal("400.00"), "food": Decimal("10.00")}
        assert Report(self.store(tmp_path)).over_budget(limits) == ["food", "rent"]

    def test_over_budget_skips_a_category_at_exactly_its_limit(self, tmp_path: Path) -> None:
        limits = {"food": Decimal("15.00"), "rent": Decimal("499.99")}
        assert Report(self.store(tmp_path)).over_budget(limits) == ["rent"]

    def test_over_budget_ignores_categories_with_no_limit(self, tmp_path: Path) -> None:
        report = Report(self.store(tmp_path))
        assert report.over_budget({"food": Decimal("1.00")}) == ["food"]
        assert report.over_budget({}) == []
