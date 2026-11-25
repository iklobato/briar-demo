from pathlib import Path

import pytest

from expenses.cli import Cli


class TestReportMonth:
    def db(self, tmp_path: Path) -> str:
        path = str(tmp_path / "e.db")
        Cli().run(["--db", path, "add", "food", "10.25", "--day", "2026-03-02"])
        Cli().run(["--db", path, "add", "rent", "500.00", "--day", "2026-03-31"])
        Cli().run(["--db", path, "add", "food", "7.00", "--day", "2026-04-01"])
        return path

    def test_prints_the_total_of_the_month(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        path = self.db(tmp_path)
        capsys.readouterr()
        assert Cli().run(["--db", path, "report", "--month", "2026-03"]) == 0
        assert capsys.readouterr().out == "total 2026-03: 510.25\n"

    def test_a_bad_month_exits_2_with_a_message(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        path = self.db(tmp_path)
        capsys.readouterr()
        assert Cli().run(["--db", path, "report", "--month", "2026-13"]) == 2
        assert "2026-13" in capsys.readouterr().err
