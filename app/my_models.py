from db.models import Model, CharField, IntegerField


class User(Model):
    name = CharField(max_length=50)
    surname = CharField(max_length=50, null=True)
    age = IntegerField(null=True)
    phone_number = CharField(max_length=20)


class Class(Model):
    name = CharField(max_length=15)
    room_number = IntegerField()
