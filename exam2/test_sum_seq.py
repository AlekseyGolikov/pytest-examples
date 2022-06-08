
import pytest
from sum_seq import seq, gen

class TestClass:
    def test_seq(self):
        assert seq(5) == [0, 1, 3, 6, 10, 1]
    def test_gen(self):
        n = 6
        g = gen(n)
        test_res = []
        try:
            while True:
                test_res.append(next(g))
        except StopIteration:
            pass
        finally:
            assert test_res == [0, 1, 2, 3, 4, 5]