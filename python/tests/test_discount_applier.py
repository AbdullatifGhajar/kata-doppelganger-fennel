from unittest.mock import MagicMock
from ..discount_applier import DiscountApplier


def assert_called_on_all_users(notifier, users):
    expected_calls = expected_calls = [
        ((user, "You've got a new discount of 10%"),) for user in users
    ]
    notifier.notify.assert_has_calls(expected_calls, any_order=True)


def discount_applier_with_notifier():
    notifier = MagicMock()
    notifier.notify = MagicMock(return_value=None)
    return notifier, DiscountApplier(notifier)


def list_of_users():
    return [MagicMock(), MagicMock(), MagicMock()]


def test_apply_v1():
    notifier, discount_applier = discount_applier_with_notifier()
    users = list_of_users()

    discount_applier.apply_v1(10, users)

    assert_called_on_all_users(notifier, users)


def test_apply_v2():
    notifier, discount_applier = discount_applier_with_notifier()
    users = list_of_users()

    discount_applier.apply_v2(10, users)

    assert_called_on_all_users(notifier, users)
