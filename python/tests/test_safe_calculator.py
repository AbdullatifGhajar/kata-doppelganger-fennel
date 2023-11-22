from unittest.mock import MagicMock

from ..safe_calculator import SafeCalculator


def test_divide_should_not_raise_any_error_when_authorized():
    authorized_authorizer = MagicMock(authorize=lambda: True)

    calculator = SafeCalculator(authorizer=authorized_authorizer)

    calculator.add(1, 2)  # no error raised
