"""
        Фикстура как фабрика данных
        Шаблон «фабрика-фикстура» может помочь в ситуациях, когда результат,
    возвращаемый фикстурой используется много раз в отдельном тесте. Суть в том, что вместо того,
    чтобы напрямую возвращать данные, фикстура возвращает функцию, которая генерирует данные.
    И затем эта функция может быть неоднократно вызвана в тесте.

    Если нужно, фабрики-фикстуры могут принимать параметры:
"""
import pytest

@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {'name': name, 'orders': []}
    return _make_customer_record

def test_customer_records(make_customer_record):
    customer_1 = make_customer_record('Lisa')
    print(customer_1)
    customer_2 = make_customer_record('Mike')
    print(customer_2)
    customer_3 = make_customer_record('John')
    print(customer_3)
