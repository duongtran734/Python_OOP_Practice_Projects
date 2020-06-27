# A decorator takes in a function, adds some functionality and returns it
# Decorators allows programmers to modify the behavior of function or class.
# Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.


# decorator with wrap function, with no arguments from the decorated function
def decorator_function(ori_func):
    def wrapper():
        print("Started")
        return ori_func()
    return wrapper

# decorator with wrap function, with  arguments from the decorated function
def decorator_function_args(ori_func):
    def wrapper(*args, **kwargs):
        print("Started")
        return ori_func(*args, **kwargs)
    return wrapper

@decorator_function
def display1():
    print("Hello")


@decorator_function_args
def display2(name,age):
    print(f"Name : {name}\nAge: {age}")



if __name__ == '__main__':
    display1()
    print()
    display2("John",25)
