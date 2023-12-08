from src.lib.func_utils import power


def test_power():
    squarer = power(2)
    assert squarer(-1) == 1
    assert squarer(0) == 0
    assert squarer(10) == 100
    cuber = power(3)
    assert cuber(1) == 1
    assert cuber(2) == 8
    assert cuber(-1) == -1
