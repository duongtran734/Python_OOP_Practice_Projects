# Class that has method that can reverse a string
class ReverseString:

    # take in a string
    def __init__(self, str=""):
        self._str = str

    # return a reverse string
    def reverse(self):
        reverse_str = ""
        for i in range(len(self._str) - 1, -1, -1):
            reverse_str += self._str[i]
        return reverse_str


if __name__ == "__main__":
    #Get string from user
    str = input("Enter the string you want to reverse: ")
    #Initialize the object
    reversed_string = ReverseString(str)
    #call the method to reverse the string from the class
    print(reversed_string.reverse())
