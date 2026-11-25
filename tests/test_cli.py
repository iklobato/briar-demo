from pathlib import Path

import pytest

from expenses.cli import Cli


class TestCli:
    def _filled(self, tmp_path: Path) -> str:
        db = str(tmp_path / "e.db")
        Cli().run(["--db", db, "add", "food", "10.00", "--day", "2026-03-04"])
        Cli().run(["--db", db, "add", "rent", "500.00", "--day", "2026-03-05"])
        return db

    def test_list_since_prints_only_expenses_on_or_after_the_day(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        db = self._filled(tmp_path)

        assert Cli().run(["--db", db, "list", "--since", "2026-03-05"]) == 0
        assert [line.split()[1] for line in capsys.readouterr().out.splitlines()] == ["rent"]

    def test_list_without_since_prints_all_expenses(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        db = self._filled(tmp_path)

        assert Cli().run(["--db", db, "list"]) == 0
        assert [line.split()[1] for line in capsys.readouterr().out.splitlines()] == ["food", "rent"]
