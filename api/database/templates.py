# Document templates for collections added to the Mongo database
#
# Documents in the database can be queried by any member 
# variable declared in the document class, or by the unique
# ObjectId generated by mongo

import mongoengine
from datetime import datetime

# Represent a user and contains relevant metadata
class Users(mongoengine.Document):
    first_name = mongoengine.StringField(max_length = 50)
    last_name = mongoengine.StringField(max_length = 50)
    email = mongoengine.EmailField(required = True, unique = True)
    password = mongoengine.StringField(requred = True, min_length = 8)


# Represents the amount a user owes to the owed user in the parent document
class Split(mongoengine.EmbeddedDocument):
    user = mongoengine.ReferenceField(Users, required = True)
    diff = mongoengine.IntField(required = True)

# Hold the information for 1 purchase
# Each purchase contains a list of splits to show how much each individual user owes
# The sum of all splits in a transaction is expected to be 0
class Transactions(mongoengine.EmbeddedDocument):
    owed_user = mongoengine.ReferenceField(Users, required = True)
    cost = mongoengine.IntField(required = True)
    diffs = mongoengine.EmbeddedDocumentListField(Split)
    description = mongoengine.StringField()
    timestamp = mongoengine.DateTimeField(default = datetime.utcnow)

# Hold information when a from_user directly pays to_user user
class Repayments(mongoengine.EmbeddedDocument):
    from_user = mongoengine.ReferenceField(Users, required = True)
    to_user = mongoengine.ReferenceField(Users, required = True)
    amount = mongoengine.IntField(required = True)
    timestamp = mongoengine.DateTimeField(default = datetime.utcnow)

# Represents a group of users sharing a ledger
class Groups(mongoengine.Document):
    name = mongoengine.StringField(max_length = 50)
    users = mongoengine.ListField(mongoengine.ReferenceField(Users), required = True)
    admin = mongoengine.ReferenceField(Users, required = True)
    ledger = mongoengine.EmbeddedDocumentListField(Transactions)
    payments = mongoengine.EmbeddedDocumentListField(Repayments)
    # TODO cache an overall split?
