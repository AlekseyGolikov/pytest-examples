"""
    Модальность: использование фикстур фикстурами
    Фикстуры могут использоваться не только тестовыми функциями, но и другими фикстурами.
    Это помогает cделать тесты модальными и дает возможность повторного использования
    фреймворк-зависимых фикстур во множестве проектов.
    Для примера инициализируем объект app, в котором будем использовать уже объявленный ресурс smtp_connection

    Здесь мы объявляем фикстуру app, которая принимает ранее объявленную фикстуру smtp_connection
    и создает с ее помощью объект App

    Поскольку фикстура smtp_connection параметризована, тест запустится дважды с разными экземплярами
    приложения App и соответствующими им серверами smtp. Нам не нужно параметризовать smtp_connection
    в фикстуре app, так как pytest самостоятельно анализирует граф зависимостей.

    Обратите внимание, что фикстура app имеет уровень модуля и использует фикстуру smtp_connection
    того же уровня. Пример будет работать и в том случае, если smtp_connection будет кэшироваться
    на уровне сессии: для фикстур нормально использовать другие фикстуры с более обширной областью действия,
    но не наоборот - фикстура уровня сессии не может полноценно использовать фикстуру уровня модуля.
"""
import pytest
import smtplib

@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print("finalizing {}".format(smtp_connection))
    smtp_connection.close()

class App:

    def __init__(self, smtp_connection):
        self._smtp_connection = smtp_connection

@pytest.fixture(scope='module')
def app(smtp_connection):
    return App(smtp_connection)

def test_smtp_connection_exists(app):
    assert app._smtp_connection
