"""Totals of the expenses in a store."""

from __future__ import annotations

from datetime import date, timedelta
from decimal import Decimal

from expenses.store import Store


class Report:
    def __init__(self, store: Store) -> None:
        self._store = store

    def by_category(self) -> dict[str, Decimal]:
        totals: dict[str, Decimal] = {}
        for expense in self._store.all():
            totals[expense.category] = totals.get(expense.category, Decimal("0")) + expense.amount
        return dict(sorted(totals.items()))

    def month_total(self, year: int, month: int) -> Decimal:
        first = date(year, month, 1)
        after = (first + timedelta(days=32)).replace(day=1)
        return sum((expense.amount for expense in self._store.all() if first <= expense.day <= after), Decimal("0"))

    def biggest(self) -> str:
        totals = self.by_category()
        return max(totals, key=lambda category: totals[category])


def top_three(report: Report) -> list[str]:
    """The three categories with the biggest totals."""
    totals = report.by_category()
    return sorted(totals, key=lambda category: totals[category])[:3]
