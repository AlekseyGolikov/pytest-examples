"""
    Использование фикстур в классах, модулях и проектах
    Декоратор usefixtures
    Фикстура cleandir будет инициализироваться для выполнения каждого тестового метода.

    Также можно «прицепить» несколько фикстур сразу
                @pytest.mark.usefixtures("cleandir", "anotherfixture")
                def test():
                    ...
    и определять использование фикстуры на уровне модуля, используя возможности механизма маркировки:
                pytestmark = pytest.mark.usefixtures("cleandir")
    Обратите внимание, что переменная должна называться именно pytestmark; если вы назовете ее, например, foomark,
    ваша фикстура инициализироваться не будет.
    Можно также затребовать вашу фикстуру для всех тестов проекта, указав в «ini»-файле:
                # content of pytest.ini
                [pytest]
                usefixtures = cleandir
"""
import os
import pytest

@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:

    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open('myfile', 'w') as f:
            f.write('hello')

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []