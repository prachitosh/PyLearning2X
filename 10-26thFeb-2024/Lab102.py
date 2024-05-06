class Password:
    def __init__(self, password):
        self.__password = password
        self.public_var = 10

    # F(n) and GET and SET

    def get_password(self, is_auth):
        if is_auth:
            return self.__password
        else:
            return "Invalid password"

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
            print("Password set successfully")
        else:
            print("Not allowed, weak password")


pwd = Password("Hacker123")
print(pwd.get_password(True))
pwd.set_password("pramod12112122")
