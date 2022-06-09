
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

c = Cl()
c.name = 5
print(c.name)
c.name = 555
print(c.name)
del c.name
func(c)

def add(n):
    if not isinstance(n, int):
        raise TypeError

def cmp(x, y):
    if x != y:
        raise ValueError
