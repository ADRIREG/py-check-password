import pytest
from app.main import check_password


def test_valid_password() -> None:
    assert check_password('Pass@word1') is True


def test_short_password() -> None:
    assert check_password('qwerty') is False


def test_long_password() -> None:
    assert check_password('Qwer2345vfg@drtrr4558896757875777') is False


def test_non_valid_password() -> None:
    assert check_password('Str@ng') is False


def test_at_least_1_digit() -> None:
    assert check_password('Stong@Password') is False


def test_at_least_1_special() -> None:
    assert check_password('StongPassword1') is False


def test_at_least_1_upper() -> None:
    assert check_password('stongpassword@1') is False


def test_max_16_characters() -> None:
    assert check_password('1AB12cd23@#34444') is True


def test_min_8_characters() -> None:
    assert check_password('ABcD12@#') is True