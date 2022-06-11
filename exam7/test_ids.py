"""
        Числа, строки, логические значения и значение None имеют свои строковые представления,
    которые используются в ID теста. Для остальных объектов pytest создает строку,
    основываясь на имени аргумента. С помощью ключевого слова ids можно самостоятельно
    определить строку, которая будет использоваться в ID теста для определенного значения фикстуры
        Пример выше показывает, что ids можно определять как списком строк, так и функцией,
    которая будет вызвана со значением фикстуры и вернет строку. В последнем случае,
    если функция вернет None, то pytest сгенерирует ID автоматически/
        При запуске тестов из примеров выше будут сгенерированы следующие ID:
    <Module test_ids.py>
  <Function test_a[spam]>
  <Function test_a[ham]>
  <Function test_b[eggs]>
  <Function test_b[1]>
<Module test_api.py>
  <Function test_ehlo[smtp.gmail.com]>
  <Function test_noop[smtp.gmail.com]>
  <Function test_ehlo[mail.python.org]>
  <Function test_noop[mail.python.org]>
"""
import pytest

def test_a(a):
    pass

def test_b(b):
    pass