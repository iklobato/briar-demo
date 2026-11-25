from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest

from expenses.cli import Cli
from expenses.store import Expense, Store


class TestExport:
    def test_writes_a_header_and_one_row_per_expense_in_day_order(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        db = tmp_path / "e.db"
        store = Store(db)
        store.add(Expense(date(2026, 3, 9), "food", Decimal("4.5"), "lunch, late"))
        store.add(Expense(date(2026, 3, 1), "rent", Decimal("500"), "march"))

        assert Cli().run(["--db", str(db), "export"]) == 0

        assert capsys.readouterr().out == (
            "day,category,amount,note\n"
            "2026-03-01,rent,500.00,march\n"
            '2026-03-09,food,4.50,"lunch, late"\n'
        )

    def test_an_empty_store_writes_only_the_header(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert Cli().run(["--db", str(tmp_path / "e.db"), "export"]) == 0

        assert capsys.readouterr().out == "day,category,amount,note\n"
