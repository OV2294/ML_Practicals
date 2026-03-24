# function to test
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# pytest test cases
def test_add():
    assert add(2, 3) == 5  # passes

def test_subtract():
    assert subtract(5, 3) == 2  # passes

def test_fail_example():
    assert add(2, 2) == 4  # this will FAIL

#To run program
#pytest test_math.py