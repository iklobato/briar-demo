# briar-demo

A tiny repo for the briar and bcc demos: `hello.py` and a small expense tracker in `expenses/`.

## Expenses

    python3 -m expenses.cli --db my.db add food 12.50 --note lunch
    python3 -m expenses.cli --db my.db list
    python3 -m expenses.cli --db my.db report

Tests: `python3 -m pytest -q`.
