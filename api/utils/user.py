from flask_login import UserMixin
# Interface class to represent a user.
# A User object must be initialized with an email

# email: the unique identifier (i.e. email) describing the User
# first_name: (optional) the User's first name
# last_name: (optional) the user's last name
# password: (optional) the encoded password used to authenticate the User
# id_num: (optional) the unique id number associated with this iser
class User(UserMixin):
    # TODO: refactor with kwargs
    def __init__(self, email, first_name = None, last_name = None, password = None, id_num = None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.id_num = id_num

    # override of get_id to return the id_num (as a string)
    def get_id(self):
        return str(self.id_num)

    # function that serializes the site-safe data for http requests
    # obviously this should not return the password, in any form
    def serialize(self):
        json = {}
        json['firstName'] = self.first_name
        json['lastName'] = self.last_name
        json['email'] = self.email
        return json

# required fields for registering a user
register_requirements = ['firstName',
                         'lastName',
                         'email',
                         'password',]
