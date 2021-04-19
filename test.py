from userData import UserData
from firebase_admin import db

user1 = UserData(name=input("Name: "), email=input("Email: "), phone=input("Phone: "), age=input("Age: "))
if db._http_client == 1:
    print("")

print(user1.get_name())
print(user1.get_email())
print(user1.get_phone())
print(user1.get_age())
