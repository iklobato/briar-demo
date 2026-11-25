from pathlib import Path

import pytest

from expenses.cli import Cli


class TestCli:
    def test_version_prints_the_version(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        assert Cli().run(["--db", str(tmp_path / "e.db"), "version"]) == 0
        assert capsys.readouterr().out == "expenses 0.1.0\n"
