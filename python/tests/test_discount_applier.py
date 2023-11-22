from unittest.mock import MagicMock
from ..discount_applier import DiscountApplier


class User:
    def __init__(self):
        self.notification = None


class Notifier:
    def notify(self, user, message):
        user.notification = message


def test_apply_v1():
    notifier = MagicMock()
    notifier.notify = MagicMock(return_value=None)
    discount_applier = DiscountApplier(notifier)
    users = [MagicMock(), MagicMock(), MagicMock()]

    discount_applier.apply_v1(10, users)

    expected_calls = expected_calls = [
        ((user, "You've got a new discount of 10%"),) for user in users
    ]
    notifier.notify.assert_has_calls(expected_calls, any_order=True)


def test_apply_v2():
    notifier = MagicMock()
    notifier.notify = MagicMock(return_value=None)
    discount_applier = DiscountApplier(notifier)
    users = [MagicMock(), MagicMock(), MagicMock()]

    discount_applier.apply_v2(10, users)

    expected_calls = expected_calls = [
        ((user, "You've got a new discount of 10%"),) for user in users
    ]
    notifier.notify.assert_has_calls(expected_calls, any_order=True)
