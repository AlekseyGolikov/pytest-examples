"""
    Источник: https://pytest-docs-ru.readthedocs.io/ru/latest/fixture.html
"""
import pytest

@pytest.mark.skipif(True, reason='отключено')
def test_connect(http_connection):
    response = http_connection
    print(response)
    assert response.status_code == 200
#///////////////////////////////////////////////////////////////////////////////
"""
    Фикстура реализует механизм открытия (start) и закрытия (teardown) обработки тестовой функции
    Если scope='function', то start и teardown будут выполнены для каждой тестовой функции
    Если scope='module', то start и teardown будут выполнены start - для первой функции, 
    teardown - для последней тестовой функции
"""
@pytest.mark.skipif(False, reason='отключено')
def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    # assert b"smtp.gmail.com" in msg
    # assert 0 # в демонстрационных целях
@pytest.mark.skipif(False, reason='отключено')
def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    # assert 0  # в демонстрационных целях
#///////////////////////////////////////////////////////////////////////////////
"""
    Фикстура реализует механизм открытия (start) и закрытия (teardown) обработки тестовой функции
"""
@pytest.mark.skipif(True, reason='отключено')
def test_file_input(open_file):
    # while True:
        f = open_file
        while True:
            _str = f.readline().replace('\r\n','')
            raise ValueError
            if _str == '':
                break
            print(_str)

# //////////////////////////////////////////////////////////////////////////
"""
    Фикстура может принимать объект для анализа контекста запрашивающей тестовой функции, класса или модуля.
    Работа фикстуры реализована на примере передачи в фикстуру объекта request
"""
smtpserver = "mail.python.org"  # будет прочитан фикстурой smtp_connection
@pytest.mark.skipif(True, reason='отключено')
def test_showhelo(smtp_connection):
    assert 0, smtp_connection.helo()
