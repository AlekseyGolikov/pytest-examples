"""
    Автоматическая группировка тестов экземплярами фикстур
    pytest минимизирует число активных фикстур во время выполнения теста.
    Если у вас есть параметризованная фикстура, то каждый экземпляр теста, ее использующий,
    сначала запускается с очередным параметром, а затем вызывает финализатор прежде,
    чем слудующий объект фикстуры будет инициализирован. Это, как и другие предоставляемые возможности,
    облегчает тестирование приложений, которые создают и используют глобальные состояния.

    Следующий пример использует две параметризованные фикстуры, одна из которых имеет уровень модуля,
    и обе функции вызывают print, чтобы продемонстрировать поток инициализации/завершения.

    Вы можете увидеть, что параметризация фикстуры modarg на уровне модуля привела к выполнению тестов в порядке,
    позволяющем минимизировать «активные» ресурсы. Финализатор фикстуры с параметром mod1 был вызван
    до инициализация фикстуры с параметром mod2.


"""
import pytest


@pytest.fixture(scope='module', params=['mod1', 'mod2'])
def modarg(request):
    param = request.param
    print('   SETUP modarg', param)
    yield param
    print('   TEARDOWN modarg', param)


@pytest.fixture(scope='function', params=[1, 2])
def otherarg(request):
    param = request.param
    print('   SETUP otherarg', param)
    yield param
    print('   TEARDOWN otherarg', param)


def test_0(otherarg):
    print('   RUN test0 with otherarg', otherarg)


def test_1(modarg):
    print('   RUN test1 with modarg', modarg)


def test_2(otherarg, modarg):
    print('   RUN test2 with otherarg {} and modarg {}'.format(otherarg, modarg))
