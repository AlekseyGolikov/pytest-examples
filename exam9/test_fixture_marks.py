"""
    Использование маркировки с параметризованными фикстурами
    pytest.param можно использовать для маркировки значений параметров параметризованных фикстур,
    точно так же, как и с @pytest.mark.parametrize.
"""
import pytest

"""
    При выполнении этого теста вызов data_set со значением 2 будет пропущен (skipped).
"""
@pytest.fixture(params=[0, 1, pytest.param(0, marks=pytest.mark.skip)])
def data_set(request):
    return request.param

def test_data(data_set):
    pass
