
def seq(n):
    def sum(i):
        sum = 0
        for j in range(i):
            sum += j
        yield sum


    def count():
        try:
            while True:
                for i in range (1, n+1):
                    yield from sum(i)
                else:
                    raise StopIteration
        except StopIteration:
            pass

    res = []
    c = count()
    try:
        while True:
            res.append(next(c))
    except Exception as ex:
        print(ex)
    finally:

        print('Счет окончен!')
        return res

n = 5
print(seq(n))

def gen(n):
    for i in range(n):
        yield i