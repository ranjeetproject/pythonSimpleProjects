import random


class Email:

    __firstName = ''
    __lastName = ''
    __password = ''
    __department = ''
    __email = ''
    __defultPasswordLength = 8
    __mailboxCapacity = 0
    __alernateEmail = ''
    __companySuffix = 'xyzCompany.com'

    def __init__(self, fname, lname):
        self.__firstName = fname
        self.__lastName = lname

        self.__department = self.__setDepartment()

        self.__password = self.__randomPassword(self.__defultPasswordLength)
        print(f"Your Password: {self.__password}")

        self.__email = self.__firstName.lower() + '.' + self.__lastName.lower() + '@' + \
            self.__department + '.' + self.__companySuffix

    def __setDepartment(self):
        print(f"Department Code \n 1 for Sale \n 2 for Development \n 3 for Accounting \n 0 for none \n Enter a Department Code")
        dep_choice = int(input("Select Any One"))
        if dep_choice == 1:
            return "Sale"
        elif dep_choice == 2:
            return "Dev"
        elif dep_choice == 3:
            return "Accountant"
        else:
            return " "

    def __randomPassword(self, size):
        passwordSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
        for x in range(0, size):
            password = ""
        for x in range(0, size):
            password_char = random.choice(passwordSet)
            password = password + password_char
        return password

    def setMailboxCapacity(self, capacity):
        self.__mailboxCapacity = capacity

    def setAlternateEmail(self, altEmail):
        self.__alernateEmail = altEmail

    def changePassword(self, psw):
        self.__password = psw

    def getMailboxCapacity(self):
        return self.__mailboxCapacity

    def getAlternateEmail(self):
        return self.__alernateEmail

    def getPassword(self):
        return self.__password

    def showInfo(self):
        return f"Display Name: {self.__firstName} {self.__lastName} \n Company Email: {self.__email} \n MailBox Capacity:  {self.__mailboxCapacity}"


email = Email("Ranjeet", "Yadav")
print(email.showInfo())
