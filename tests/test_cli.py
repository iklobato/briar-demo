from pathlib import Path

import pytest

from expenses.cli import Cli


class TestCliList:
    def _filled(self, tmp_path: Path) -> str:
        db = str(tmp_path / "e.db")
        Cli().run(["--db", db, "add", "food", "10.00", "--day", "2026-03-02"])
        Cli().run(["--db", db, "add", "rent", "500.00", "--day", "2026-03-03"])
        return db

    def test_a_category_lists_only_its_expenses(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        db = self._filled(tmp_path)

        assert Cli().run(["--db", db, "list", "--category", "food"]) == 0
        assert capsys.readouterr().out == "2026-03-02 food 10.00 \n"

    def test_without_a_category_every_expense_is_listed(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        db = self._filled(tmp_path)

        assert Cli().run(["--db", db, "list"]) == 0
        assert capsys.readouterr().out == "2026-03-02 food 10.00 \n2026-03-03 rent 500.00 \n"
