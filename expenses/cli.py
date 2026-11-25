"""The command line: add, list and report expenses kept in a sqlite file."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

from expenses.money import Money
from expenses.report import Report
from expenses.store import Expense, Store


class Cli:
    def run(self, argv: list[str]) -> int:
        args = self._parser().parse_args(argv)
        if args.command == "version":
            sys.stdout.write("expenses 0.1.0\n")
            return 0
        store = Store(Path(args.db))
        commands = {"add": self._add, "list": self._list, "report": self._report}
        return commands[args.command](store, args)

    def _parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(prog="expenses")
        parser.add_argument("--db", default="expenses.db")
        sub = parser.add_subparsers(dest="command", required=True)
        add = sub.add_parser("add")
        add.add_argument("category")
        add.add_argument("amount")
        add.add_argument("--note", default="")
        add.add_argument("--day", default="")
        sub.add_parser("list")
        sub.add_parser("report")
        sub.add_parser("version")
        return parser

    def _add(self, store: Store, args: argparse.Namespace) -> int:
        day = date.fromisoformat(args.day) if args.day else date.today()
        store.add(Expense(day, args.category, Money().parse(args.amount), args.note))
        return 0

    def _list(self, store: Store, args: argparse.Namespace) -> int:
        for expense in store.all():
            sys.stdout.write(f"{expense.day} {expense.category} {Money().shown(expense.amount)} {expense.note}\n")
        return 0

    def _report(self, store: Store, args: argparse.Namespace) -> int:
        report = Report(store)
        for category, total in report.by_category().items():
            sys.stdout.write(f"{category}: {Money().shown(total)}\n")
        sys.stdout.write(f"biggest: {report.biggest()}\n")
        return 0


if __name__ == "__main__":
    raise SystemExit(Cli().run(sys.argv[1:]))
