"""Money as Decimal: parse what a person types, show it back."""

from __future__ import annotations

from decimal import Decimal, InvalidOperation


class MoneyError(ValueError):
    """A text that is not an amount of money."""


class Money:
    CENTS = Decimal("0.01")

    def parse(self, text: str) -> Decimal:
        cleaned = text.strip().replace(",", "")
        try:
            amount = Decimal(cleaned)
        except InvalidOperation as broken:
            raise MoneyError(f"not an amount: {text!r}") from broken
        return amount.quantize(self.CENTS)

    def shown(self, amount: Decimal) -> str:
        return f"{amount.quantize(self.CENTS)}"


def parse_signed(text: str) -> Decimal:
    """An amount that may carry a dollar sign."""
    return Money().parse(text.replace("$", ""))
