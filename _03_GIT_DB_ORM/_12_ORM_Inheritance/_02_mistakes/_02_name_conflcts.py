class A:
    def method(self):
        print('Метод класса А')


class B:
    def method(self):
        print('Метод класса Б')


# class C(A, B):
#     pass

class C(A, B):
    def method(self):
        super().method()
        B.method(self)


if __name__ == '__main__':
    obj = C()
    obj.method()
