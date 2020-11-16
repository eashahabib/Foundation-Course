# Utils Python module 

# Palindrome checker function
def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

# Person class
class Person:
    def __init__(self, greeting):
        self.greeting = greeting
    def greet(self):
        print(self.greeting)
