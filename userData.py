
class UserData:
    # great
    def __init__(self, name, email, phone, age):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


user1 = UserData(name=input("Name: "), email=input("Email: "), phone=input("Phone: "), age=input("Age: "))

print(user1.get_name())
print(user1.get_email())
print(user1.get_phone())
print(user1.get_age())


