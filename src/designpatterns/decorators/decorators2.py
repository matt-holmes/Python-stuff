#decorators.py

def is_logged_in(func):
    def wrapper(logged_in):
        if logged_in:
            return func()
        else:
            return logged_in
    return wrapper

@is_logged_in
def generate_view():
    return "Hello"


def test_decorator():
    assert generate_view(True) == 'Hello'
    assert generate_view(False) == False
