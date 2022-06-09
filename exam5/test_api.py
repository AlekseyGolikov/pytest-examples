# Параметрическое тестирование
import types

import api
import pytest

skip_fl = True

@pytest.mark.skipif(skip_fl,reason='отключено')
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54), ('5/5', 1), ('8-4', 4)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.mark.skipif(skip_fl,reason='отключено')
@pytest.mark.parametrize('test_values, expected', [((1,2), 2), ((2,2), 4), ((3,3), 6)])
def test_sum_nums(test_values, expected):
    assert api.sum_nums(test_values[0], test_values[1]) == expected

@pytest.mark.skipif(skip_fl, reason='отключено')
@pytest.mark.parametrize('n, expected', [(5, (1, 2, 3)),
                               (6, (1, 2, 3, 5)),
                               (7, (1, 2, 3, 5, 8)),
                               (8, (1, 2, 3, 5, 8, 13)),
                               (9, (1, 2, 3, 5, 8, 13, 21)),
                               (10, (1, 2, 3, 5, 8, 13, 21, 34))])
def test_fibonacchi(n, expected):
    fibo = api.fibonacci(n)
    for i in range(1, n-1):
        assert next(fibo) == expected[i-1]

@pytest.mark.skipif(skip_fl, reason='отключено')
@pytest.mark.parametrize('seq, expected', [((1, (2, (3, 4), 5), 6), [1, 2, 3, 4, 5, 6]),
                                           (((7, 8), 9, (10, 11), 12, 13), [7, 8, 9, 10, 11, 12, 13]),
                                           (((14, (15, 16), (17, (18, (19, (20, 21)))))), [14, 15, 16, 17, 18, 19, 20, 21])])
def test_filter_seq(seq, expected):
    res = []
    for i in range(3):
        g = api.filter_list(seq)
        try:
            while True:
                res.append(next(g))
        except StopIteration:
            # assert res == expected
            print(res)
            res.clear()

@pytest.mark.slippy_average
class TestSlippyAverage:

    def test__enter__(self):
        with api.SlippyAverage() as test_av:
            assert type(test_av) == types.GeneratorType, 'Функция __enter__() должна возвращать объект генератора!'

    @pytest.mark.parametrize('n, expected', [
                                             (8, [2.5, 3.5, 4.5, 5.5]),
                                             (9, [2.5, 3.5, 4.5, 5.5, 6.5]),
                                             (10, [2.5, 3.5, 4.5, 5.5, 6.5, 7.5]),
                                             (11, [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]),
                                             (12, [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5])
                                            ])
    def test_get_res(self, n, expected):
        with api.SlippyAverage() as test_av:
            res = []
            for i in range(1, n):
                token = (4, i)
                _res = test_av.send(token)
                if i >= 4:
                    res.append(_res)
            else:
                assert res == expected
                # print(res)


if __name__ == '__main__':
    t = TestSlippyAverage()
    t.test_get_res(8, [2.5, 3.5, 4.5, 5.5])
