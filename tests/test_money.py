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


class TestCents:
    def test_an_amount_becomes_whole_cents(self) -> None:
        from expenses.money import cents

        assert (cents(Decimal("12.34")), cents(Decimal("0")), cents(Decimal("5"))) == (1234, 0, 500)
