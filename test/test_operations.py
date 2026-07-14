from test.operations import sub2, sum2


def test_sum2():
    assert sum2(10, 2) == 12
    assert sum2(-4, -3) == -7




def test_sub2():
    assert sub2(1, 4) == -3
    assert sub2(5, -5) == 10
