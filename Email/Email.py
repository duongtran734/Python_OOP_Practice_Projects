'''
Email Application

Scenario: You are an IT support Administration Specialist and are charged with the task of creating email accounts or new hires.

Your application should do the following:
 - Generate an email with the following syntax: firstname.lastname@department.company.com
 -Determine the department(sales,development,accounting), if non leave blank
 - Generate a random String for a password
 - Have a set methods to change the password, set the mailbox capacity, and define an alternate email address
 - Have get methods to display the name, email ,mailbox capacity
'''

import random

class Email:

    _alter_email =""

    def __init__(self, firstname, lastname):
        self._firstname  = firstname
        self._lastname = lastname
        self._department = self.department()
        self._password = self.password_generater()
        self._company = self.get_company()
        self._email = self.generate_email()
        self._mailbox_capacity = 100

    # Get what department user is in
    def department(self):
        try:
            valid = [1,2,3]
            while 1:
                choice = int(input(f"New Worker: {self._firstname}\nEnter your department:\n1 - Sales\n2 - Development\n3 - Accounting:\n"))
                if choice in valid:
                    if choice == 1:
                        return "Sales"
                    elif choice == 2:
                        return "Development"
                    elif choice == 3:
                        return "Accounting"
                else:
                    print("Invalid input")
        except Exception:
            print("Invalid input")
    # Generate a random password for user depending on the user choice of length
    def password_generater(self):
        pw = "ABCDEFGHIJGLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwxyz123456789"
        pw_length = int(input("Enter the length of your password:"))
        password = ""
        for i in range(0,pw_length):
            password += random.choice(pw)
        return password
    # Get company name from user
    def get_company(self):
        return input("What's your company name:")
    # Generate employee email
    def generate_email(self):
        email= f"{self._firstname}.{self._lastname}@{self._department}.{self._company}.com"
        return email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def mb_capacity(self):
        return self._mailbox_capacity

    @mb_capacity.setter
    def mb_capacity(self, new_capacity):
        self._mailbox_capacity = new_capacity

    @property
    def alterEmail(self):
        return self._alter_email

    @alterEmail.setter
    def alterEmail(self, alter_email):
        self._alter_email = alter_email

    def show(self):
        print(f'''Name : {self._firstname} {self._lastname}\nEmail : {self.email}\nMailbox Capacity: {self._mailbox_capacity}               
        ''')
if __name__ == "__main__":
    email1 = Email("John", "Smith")
    email1.show()

