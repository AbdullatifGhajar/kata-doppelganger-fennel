import pytest

from ..safe_calculator import SafeCalculator

class AuthorizedAuthorizer:
    def authorize(self):
        return True
    
def test_divide_should_not_raise_any_error_when_authorized():
    calculator = SafeCalculator(authorizer=AuthorizedAuthorizer())
    
    calculator.add(1, 2) # no error raised

    
    
    
