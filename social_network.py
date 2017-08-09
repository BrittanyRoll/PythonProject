import turtle
import math

class User:

    def _init_(self, name):
        self.user_name = name
        self.age = 0
        self.interests = []
        self.friends = []

    def get_name(self):
        return self.user_name    #shows name

    def change_age(self, age):
        self.age = age          #change age

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
    def _init_(self, ):
        self.profile
        self.all_users = []

    def users(self, friends):
        


def main():



if _name_ == '_main_'
