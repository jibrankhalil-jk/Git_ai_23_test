import pytest
from calculator import Calculator


@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2),
    (0, 0, 0)
])
def test_sub_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (0, 28, 0),
    (111111111000000, 1, 111111111000000),
    (99999999, 99999999, 9999999800000001),
    (-10, 2, -20),
    (-10, -2222, 22220),
    (2.323, 1.987, 4.615801),
    (8.23, 323.342423423423423, pytest.approx(2661.1081447748)),
    (0, 0, 0)
])
def test_mul_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (50, 5, 10),
    (33, 16, 2.0625),
])
def test_div_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.divide(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (4, 4, 256),
    (2, -1, 0.5),
])
def test_pow_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.power(a, b) == expected


@pytest.mark.parametrize("n, expected", [
    (0,1), 
    (1,1), 
    (2,2), 
    (10,3628800),  
])
def test_factorial_parameterized(n, expected):
    calc = Calculator()
    assert calc.factorial(n) == expected

def test_factorial():
    calc = Calculator() 
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calc.factorial(-22)


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (10, 55)
])
def test_fibonacci_parameterized(n, expected):
    calc = Calculator()
    assert calc.fibonacci(n) == expected

def test_fibonacci():
    calc = Calculator() 
    with pytest.raises(ValueError, match="Fibonacci is not defined for negative numbers"):
        calc.fibonacci(-2)



# def test_add():
#     calc = Calculator()
#     assert calc.add(3, 5) == 8
#     assert calc.add(-1, 1) == 0
#     assert calc.add(-1, -1) == -2


# def test_subtract():
#     calc = Calculator()
#     assert calc.subtract(5, 3) == 2
#     assert calc.subtract(1, 5) == -4
#     assert calc.subtract(-5, -3) == -2


# def test_multiply():
#     cal = Calculator()
#     # for integer
#     assert cal.multiply(0, 28) == 0
#     assert cal.multiply(111111111000000, 1) == 111111111000000
#     assert cal.multiply(99999999, 99999999) == 9999999800000001
#     assert cal.multiply(-10, 2) == -20
#     assert cal.multiply(-10, -2222) == 22220
#     # for floating point numbers
#     assert cal.multiply(2.323, 1.987) == 4.615801
#     assert cal.multiply(
#         8.23, 323.342423423423423) == pytest.approx(2661.1081447748)


# def test_divide():
#     calc = Calculator()
#     # Normal division (like 10/2)
#     assert calc.divide(50, 5) == 10
#     #  Division with decimals (like 5/2)
#     assert calc.divide(33, 16) == 2.0625
#     #  Division by zero (what should happen?)
#     with pytest.raises(ValueError, match="Cannot divide by zero"):
#         calc.divide(99, 0)
