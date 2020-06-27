import string

class StringUpperLower:

    def __init__(self, str):
        self._str = str

    # Get the str
    @property
    def str(self):
        return self._str

    # Set the str
    @str.setter
    def set_str(self, new_str):
        self._str = new_str

    # return the given str to uppercase
    def string_upper(self):
        return self._str.upper()
    # return the given str in lowercase
    def string_lower(self):
        return self._str.lower()


if __name__ == "__main__":
    str = "Hello World"

    #Initialize the object
    str_obj = StringUpperLower(str)

    # Call the method from the class


    #Using Setter Method
    str_obj.set_str = "New String"
    #Using getter Method
    print(str_obj.str)