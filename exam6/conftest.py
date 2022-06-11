"""
    Источник: https://pytest-docs-ru.readthedocs.io/ru/latest/fixture.html
"""
import pytest
import requests
import smtplib

@pytest.fixture(scope='function')
def http_connection():
    url = 'https://yandex.ru/'
    return requests.get(url=url)
# //////////////////////////////////////////////////////////////////////////
"""
    Фикстура реализует механизм открытия (start) и закрытия (teardown) обработки тестовой функции
    Если scope='function', то start и teardown будут выполнены для каждой тестовой функции
    Если scope='module', то start и teardown будут выполнены start - для первой функции, 
    teardown - для последней тестовой функции
"""
@pytest.fixture(scope='function')       # scope = 'function' - фикстура будет выполняться (start и teardown) для каждой функции отдельно
                                        # scope = 'module' - фикстура будет выполняться (start и teardown) один раз для всего модуля
                                        # scope = 'session' - фикстура будет выполняться (start и teardown) один раз для сессии
                                        # scope = 'cls' - фикстура будет выполняться (start и teardown) один раз для всего класса
def smtp_connection():
    print('start', end=' ')  # имитация фикстурой метода start
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp_connection:
        yield smtp_connection    # если нет необходимость в завершении расширения тестовой функции то yield следует заменить на return
    print(' teardown smtp', end='')   # имитация фикстурой метода teardown
    smtp_connection.close()
# //////////////////////////////////////////////////////////////////////////
"""
    Фикстура реализует механизм открытия (start) и закрытия (teardown) обработки тестовой функции
"""
@pytest.fixture(scope='function')
def open_file():
    print('start')
    with open('text.txt') as f:
        yield f
    print('tear down')
# //////////////////////////////////////////////////////////////////////////
"""
    Фикстура может принимать объект для анализа контекста запрашивающей тестовой функции, класса или модуля.
    Работа фикстуры реализована на примере передачи в фикстуру объекта request
"""
@pytest.fixture(scope='module')
def smtp_connection2(request):
    # print(type(request))
    server = getattr(request.module, 'smtpserver', 'smtp.gmail.com')
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print('finalizing {} ({})'.format(smtp_connection, server))
    smtp_connection.close()


