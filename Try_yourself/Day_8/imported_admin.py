
class User():
    def __init__(self, first_name, last_name, *user_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = user_profile

    def describe_user(self):
        print(f'Here are the details of the User : {self.first_name.title()} {self.last_name.title()}')
        print(f'Additional information: {self.user_profile}')
    
    def greet_user(self):
        print(f'Hello {self.last_name.title()}, Hope you are doing good!!')


class Privileges():
    def __init__(self, privilages = ['can add post', 'can delete post', 'can ban user']):
        self.privilages = privilages
        
    def show_privilages(self):
        for privilages in self.privilages:
            print(privilages)


class Admin(User):

    def __init__(self, first_name, last_name, *user_profile):
        super().__init__(first_name, last_name, *user_profile)
        self.privilage_instance = Privileges()


if __name__ == "__main__":

    user_1 = Admin('sai','korumilli')
    user_1.privilage_instance.show_privilages()
