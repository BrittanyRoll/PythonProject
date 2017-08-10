import turtle
import math

class User:

    def __init__(self, name):
        self.user_name = name     #constructor
        self.age = 0
        self.interests = []
        self.friends = []

    def get_name(self):
        return self.user_name    #shows name

    def change_age(self, age):
        self.age = int(age)          #change age

    def get_age(self):
        return self.age        #shows age

    def user_name(self, name):
        self.user_name = name #change username

    def friends(self, friends):
        self.friends.append(friends)    #add friends

    def del_friends(self, enemies):
        self.friends.remove(enemies)     #delete friends

    def get_friends(self, friends):
        return self.friends

    def add_interest(self, things):
        self.interests.append(things)



class Network:
    def __init__(self):
        self.all_users = []

    def users(self, name):
        self.all_users.append(name)

    def get_users(self):
        return self.all_users

    def num_users(self):
        return (len(self.all_users))

    def add_connect(self, user1, user2):
        user1.friends(user2)
        user2.friends(user1)

    def show_connect(self):
        return (add_connect)



def main():
    print("Do you want to make a new user? (enter yes or no)")
    user_input = input()
    #key = click.getchar('y')
    #key1 = click.getchar('n')
    if user_input == "yes":
        user1 = User("Brittany")
        user2 = User("Ericka")
        network = Network()
        add_connect(user1, user2)
        show_connect()

        print("Enter your name")
        user_input = input()
        user1.user_name(user_input)
        user1.get_name()
        print("What is your age?")
        user_input = input()
        user1.age = int(user_input)
        user1.get_age
        print("Do you have any interest?")

        if user_input == "yes":
            while (user_input == "yes"):
                print("What is one interest?")
                user_input = input()
                user1.add_interest(user_input)
                print("Do you have anymore interests? (yes or no)")
                user_input = input()

        elif user_input == "no":
            print("Do you have any friends?")
            if user_input == "yes":
                while user_input == "yes":
                    print("What is one of the friend's names?")
                    user_input = input()
                    user1.friends(user_input)
                    print("Do you have anymore friends?")


            else:
                print





    else:
        exit()





#if _name_ == '_main_'

main()
