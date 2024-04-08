# extending list class

class ExtendedList(list):
    def printListInfo(self):
        print(f"List has {len(self)} elements")


customList = ExtendedList([1, 3, 45, 5])
customList.append(5)

customList.printListInfo()


class User:
    def __init__(self, username, password):
        self.password = password
        self.username = username

    def make_admin(self, role):
        return Admin(self.username, self.password, role)


class Admin(User):
    def __init__(self, username, password, role):
        super().__init__(username, password)
        self.isAdmin = True
        self.role = role


user = User("damiansoch", "damian1")
admin = Admin("kingasoch", "kinga1", "Developer")

print(user.__dict__)
print(admin.__dict__)

user_admin = user.make_admin("Administrator")

print(user_admin.__dict__)
