# Decorator Class

class decorator_class():

    def __init__(self,ori_func):
        self.ori_function = ori_func

    def __call__(self, *args, **kwargs):
        print("Started")
        return self.ori_function(*args, **kwargs)


# @class_name will make the it a decorator in python
@decorator_class
def display1():
    print("Hello")


@decorator_class
def display2(name,age):
    return print(f"Name : {name}\nAge: {age}")


if __name__ == '__main__':
    display1()
    print()
    display2("John",23)