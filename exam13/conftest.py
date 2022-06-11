"""
    Использование фикстур в классах, модулях и проектах
    Декоратор usefixtures
    Фикстура cleandir будет инициализироваться для выполнения каждого тестового метода.
"""
import os
import shutil
import tempfile
import pytest


@pytest.fixture
def cleandir():
    old_cwd = os.getcwd()
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    yield
    os.chdir(old_cwd)
    shutil.rmtree(newpath)