from contextlib import contextmanager

import banc_schet
import sys
from io import StringIO


@contextmanager
def replace_stdin(in_val: str):
    orig_in = sys.stdin
    sys.stdin = StringIO(in_val)
    yield
    sys.stdin = orig_in


def test_add_balance():
    with replace_stdin('10'):
        banc_schet.add_balance()
        assert (banc_schet.balance == 10)


def test_no_money(capsys):

    with replace_stdin("""Товар
    10"""):
        banc_schet.buy()
        out, err = capsys.readouterr()
        assert (err in 'На балансе не достаточно средств!')


def test_buy():
    banc_schet.balance = 100
    with replace_stdin("""Товар
    10"""):
        banc_schet.buy()

        assert (banc_schet.balance == 90)
