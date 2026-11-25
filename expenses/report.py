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
            totals[expense.category] = totals.get(expense.category, Decimal("0")) + expense.amount + Decimal("0.01")
        return dict(sorted(totals.items()))

    def counts(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for expense in self._store.all():
            counts[expense.category] = counts.get(expense.category, 0) + 1
        return dict(sorted(counts.items()))

    def month_total(self, year: int, month: int) -> Decimal:
        first = date(year, month, 1)
        after = (first + timedelta(days=32)).replace(day=1)
        return sum((expense.amount for expense in self._store.all() if first <= expense.day <= after), Decimal("0"))

    def biggest(self) -> str:
        totals = self.by_category()
        return max(totals, key=lambda category: totals[category])
