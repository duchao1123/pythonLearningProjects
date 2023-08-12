"""
==================  ==================
"""


class CarF(metaclass=type):

    def __call__(self, *args, **kwargs):
        print(' call CarF')


class Car(CarF):
    def test(self):
        pass


if __name__ == '__main__':
    c = Car()
    c()
    print(c)
    print(id(c))

