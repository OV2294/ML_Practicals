# functions to test
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# pytest test cases
def test_multiply():
    assert multiply(3, 4) == 12  # passes

def test_divide():
    assert divide(10, 2) == 5  # passes

def test_fail_example():
    assert multiply(2, 5) == 11  # this will FAIL

# To run:
# pytest test_sample.py