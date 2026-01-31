import pytest
from src.calculator import fun1, fun2, fun3, fun4

def test_fun1():
    assert fun1(2, 3) == 5

def test_fun2():
    assert fun2(5, 3) == 2

def test_fun3():
    assert fun3(4, 3) == 12

def test_fun4():
    # fun4 combines fun1, fun2, and fun3
    # fun1(2,3)=5, fun2(2,3)=-1, fun3(2,3)=6 → total = 10
    assert fun4(2, 3) == 10

def test_invalid_input():
    with pytest.raises(ValueError):
        fun1("a", 2)
