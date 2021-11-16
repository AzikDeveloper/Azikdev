
from app.my_models import User

if __name__ == '__main__':
    user = User(name='Asilbek', surname='Xushnazarov', age=20, phone_number='+998936676890')
    user.age = 19
    user = user.save()
    print(user)

    users = User.objects.all()
    print(users)

    user_in_2 = User.objects.get(age=19)
    print(user_in_2)
