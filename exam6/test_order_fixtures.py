"""Порядок инициализации фикстур в зависимости от значения параметра окружения scope
    Фикстуры, запрошенные функцией test_order, будут инициализированы в следующем порядке:
        s1: фикстура с самой широкой областью действия (session).
        m1: фикстура второго уровня (module).
        a1: фикстура с областью действия function (function-scoped fixture) и параметром autouse = True:
            экземпляр этой фикстуры будет создан до создания остальных function-scoped фикстур.
        f3: function-scoped фикстура, которую запрашивает функция f1: ее нужно создать в момент запроса
        f1: первая function-scoped фикстура в списке аргументов функции test_order.
        f2: последняя function-scoped фикстура в списке аргументов функции test_order.
"""
import pytest
order = []

@pytest.fixture(scope="session")
def s1():
    order.append("s1")
@pytest.fixture(scope="module")
def m1():
    order.append("m1")
@pytest.fixture
def f1(f3):
    order.append("f1")
@pytest.fixture
def f3():
    order.append("f3")
@pytest.fixture(autouse=True)
def a1():
    order.append("a1")
@pytest.fixture
def f2():
    order.append("f2")

@pytest.mark.skipif(True, reason='отключено')
def test_order(f1, m1, f2, s1):
    assert order == ["s1", "m1", "a1", "f3", "f1", "f2"]