from expenses.currencies import CODES, NAMES


def test_codes_count():
    assert len(CODES) == 177


def test_codes_unique():
    assert len(set(CODES)) == len(CODES)


def test_codes_are_three_upper_case_letters():
    for code in CODES:
        assert len(code) == 3 and code.isalpha() and code.isupper(), code


def test_names_cover_codes():
    assert set(NAMES) == set(CODES)
    assert all(NAMES[code].strip() for code in CODES)
