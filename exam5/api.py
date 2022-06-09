

class Cl:
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def del_name(self):
        del self.__name
    name = property(get_name, set_name, del_name)

def func(obj):
    if hasattr(obj, 'name'):
        raise AttributeError('Объект не должен иметь аттрибута name!')

def add(n):
    if not isinstance(n, int):
        raise TypeError

def cmp(x, y):
    if x != y:
        raise ValueError

def cmp_vars(x, y):
    return x == y

def sum_nums(x, y):
    return x + y

def fibonacci(n):
    def fibo():
        """Алгоритм Фибоначчи"""
        x0 = 0
        x1 = 1
        def next_num():
            nonlocal x0, x1
            x0, x1 = x1, x0+x1
            return x1
        return next_num

    algo = fibo()
    for i in range(2, n):
        yield algo()

def filter_list(seq):
    """
        Рекурсивный алгоритм преобразования сложного списка в простой
    """
    if not isinstance(seq, tuple):
        raise TypeError('Последовательность seq должна быть списком!')
    for x in seq:
        if not isinstance(x, int):
            yield from filter_list(x)
        else:
            yield x


class SlippyAverage:
    """
        Класс реализует метод скользящего среднего
        Задана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
        Измерения велись n секунд.
        В секунду i поступает qi запросов.
        Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.
    """
    def __init__(self):
        self.__coro = self.average_seq()

    def __enter__(self):
        x = self.__coro.__next__()
        # print(type(x))               # class 'float'
        # print(type(self.__coro))     # class 'generator'
        # print(type(self.__coro()))   # class
        return self.__coro

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__coro.close()

    def send(self, token):
        return self.__coro.send(token)

    def average_seq(self):
        buffer = []
        _sum = 0.0
        while True:
            token = yield _sum  # token = (k, step)
            buffer.append(token[1])
            if token[1] >= token[0]:
                _sum = float(sum(buffer) / token[0])
                del_el = buffer.pop(0)

if __name__ == '__main__':

# Начало - проверка алгоритма Фибоначчи
#     n = 10
#     fibo = fibonacci(n)
#     for i in range(1, n-1):
#         print(next(fibo))
# Конец - проверка алгоритма Фибоначчи

# Начало - Алгоритм преобразования сложного списка в простой
#     seq = (1, (2, 3), 4, (5, (6, (7, 8), 9), 10), 11)
#     print(seq)
#     g = filter_list(seq)
#     res = []
#     try:
#         while True:
#             res.append(next(g))
#     except StopIteration:
#         print(res)
#         print('Работа завершена!')
# Конец - Алгоритм преобразования сложного списка в простой
# Начало - Алгоритм скользящего среднего
    k = 4
    res = []
    with SlippyAverage() as av:
        for i in range(1, 10):
            token = (k, i)
            _res = av.send(token)
            if i >= 4:
                res.append(_res)
        else:
            print(res)
            print("Расчет окончен!")
# Конец - Алгоритм скользящего среднего