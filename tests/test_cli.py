from pathlib import Path

import pytest

from expenses.cli import Cli


class TestCli:
    def test_report_on_an_empty_database(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        assert Cli().run(["--db", str(tmp_path / "new.db"), "report"]) == 0
        assert capsys.readouterr().out == "no expenses\n"
