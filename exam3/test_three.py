
"""Проверим тип данный Task."""

from collections import namedtuple
import pytest
import time

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    """Без использования параметров, следует ссылаться на значения по умолчанию"""
    t1 = Task()
    print('test_defaults')
    t2 = Task(None, None, False, None)
    time.sleep(2)
    assert t1 == t2

@pytest.mark.run_this
def test_member_access():
    """Проверка свойства .field (поля) namedtuple"""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    print('test_member_access')
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)

@pytest.mark.run_this_test
def test_asdict():
    """_asdict() должен возвращать словарь."""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    print('test_asdict')
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}

    assert t_dict == expected

def test_replace():
    """должно изменить переданное в fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    print('test_replace')
    t_expected = Task('finish book', 'brian', True, 10)
    time.sleep(1)
    assert t_after == t_expected
