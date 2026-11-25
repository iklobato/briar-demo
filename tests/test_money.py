from decimal import Decimal

import pytest

from expenses.money import Money, MoneyError


class TestMoney:
    def test_an_amount_is_parsed_to_cents(self) -> None:
        assert Money().parse(" 12.5 ") == Decimal("12.50")

    def test_a_comma_thousands_separator_is_read(self) -> None:
        assert Money().parse("1,234.50") == Decimal("1234.50")

    def test_text_that_is_no_amount_is_refused(self) -> None:
        with pytest.raises(MoneyError, match="not an amount: 'abc'"):
            Money().parse("abc")

    def test_a_negative_amount_is_refused(self) -> None:
        with pytest.raises(MoneyError, match="negative amount: '-5'"):
            Money().parse("-5")

    def test_zero_is_accepted(self) -> None:
        assert Money().parse("0") == Decimal("0.00")
