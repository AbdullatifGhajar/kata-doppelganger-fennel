from ..discount_applier import DiscountApplier

class User:
    def __init__(self):
        self.notification = None

class Notifier:
    def notify(self, user, message):
        user.notification = message

def test_apply_v1():
    discount_applier = DiscountApplier(Notifier())
    users = [User(), User(), User()]
    
    discount_applier.apply_v1(10, users)
    
    for user in users:
        assert user.notification == "You've got a new discount of 10%"


def test_apply_v2():
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v2
    pass
