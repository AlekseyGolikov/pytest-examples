"""
    Фикстуры autouse (автоматическое использование фикстур)

    Иногда хочется, чтобы фикстуры вызывались автоматически, без явного указания их в качестве аргумента
    и без использования декоратора usefixtures . В качестве примера приведена фикстура, имитирующая базу данных
    с архитектурой «begin/rollback/commit» и мы хотим автоматически обернуть каждый тестовый метод транзакцией
    и откатом к начальному состоянию.

    Фикстура transact уровня класса промаркирована autouse=true, и это означает,
    что все тестовые методы класса будут использовать эту фикстуру без необходимости указывать ее в сигнатуре
    тестовой функции или использовать на уровне класса декоратор usefixtures.
    Пример:
"""

import pytest

class DB:

    def __init__(self):
        self._intransaction = []

    def begin(self, name):
        self._intransaction.append(name)

    def rollback(self):
        self._intransaction.pop()

@pytest.fixture(scope='module')
def db():
    return DB()

class TestClass:

    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        yield
        db.rollback()

    def test_method1(self, db):
        assert db._intransaction == ['test_method1']

    def test_method2(self, db):
        assert db._intransaction == ['test_method2']
