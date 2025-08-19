# Test

import pytest
from factorial_simple import factorial

@pytest.mark.parametrize("n,expected", [(0,1),(1,1),(2,2),(5,120),(10,3628800)])
def test_factorial_values(n, expected):
    assert factorial(n) == expected

@pytest.mark.parametrize("bad", [-1, -10])
def test_factorial_negative(bad):
    with pytest.raises(ValueError):
        factorial(bad)

@pytest.mark.parametrize("bad", [0.1, 1.0, "3", None, True])
def test_factorial_type_errors(bad):
    with pytest.raises(TypeError):
        factorial(bad)

if __name__ == "__main__":
    import sys, pytest
    sys.exit(pytest.main([__file__, "-q"]))