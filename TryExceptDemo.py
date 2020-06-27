class TryExceptDemo:

    def __init__(self,x , y ):
        self._x = x
        self._y = y

    def foo1(self):
        try:
            if self._x/self._y:
                print("a")
        except:
            print("b")

        else:
            print("c")

        finally:
            print("d")

    def foo2(self):
        try:
            if self._x / self._y:
                print("a")
                return
        except:
            print("b")

        else:
            print("c")

        finally:
            print("d")

    def foo3(self):
        try:
            if self._x / self._y:
                print("a")
                raise Exception("Go to Except Clause")
        except:
            print("b")

        else:
            print("c")

        finally:
            print("d")

if __name__ == '__main__':
    print("foo1")
    obj = TryExceptDemo(1, 2)
    obj.foo1()

    print("-----------------")
    obj = TryExceptDemo(1, 0)
    obj.foo1()

    print("-----------------")
    print("foo2")
    obj = TryExceptDemo(1, 2)
    obj.foo2()

    print("-----------------")
    obj = TryExceptDemo(1, 0)
    obj.foo2()

    print("-----------------")
    print("foo3")
    obj = TryExceptDemo(1, 2)
    obj.foo3()

    print("*****************")
    obj = TryExceptDemo(1, 0)
    obj.foo3()