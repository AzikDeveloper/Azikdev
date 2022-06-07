# Azikdev shell :)
# I can make tests here
from app.my_models import User

if __name__ == '__main__':
    user = User(name='Johny', surname='Samata', age=25, phone_number='+998936676890')
    user.age = 19
    user.name = 'Tony'
    user.surname = 'Sama'
    user = user.save()

    users = User.objects.all()

    for user in users.instances:
        print(user)
    print('>>')
