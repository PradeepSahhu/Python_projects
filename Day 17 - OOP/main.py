
# Creating classes in python
print("Namaste world")

# Name of our class must be Pascal Case. unlike snake_case or camelCase


class User:  # We can't have an empty class we have to input some data in it. like pass

    def __init__(self, users, user_id, username):
        """Constructor / initializer"""
        # print("calling the init function")
        self.users = users
        self.online = 0  # Default value no need to add that attribute in parameter.
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):  # Adding method in the class
        """ Trying function in a class"""
        user.followers += 1
        self.following += 1

    def unfollow(self, user):
        user.followers -= 1
        self.following -= 1


user_1 = User(users=20, user_id="001", username="pradeep sahu")  # Building an object from our class.
# user_1 = User(users="32", username="Pradeep Sahu", user_id="001")
# print(user_1.online)
# print(user_1.username)
# print(user_1.users)
# user_1.id = "001"
# user_1.username = "pradeep sahu"
# print(user_1.id)
user_2 = User(39, "002", "Ritik sahu")
# # user_2.id = "002"
# # user_2.username = "Ritik sahu"
# print(user_2.online)

# Trying the method in the class

user_1.follow(user_2)

user_2.follow(user_1)

user_1.unfollow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

print(user_2.username)