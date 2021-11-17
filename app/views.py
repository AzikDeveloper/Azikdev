from app.my_models import User
from aziktools.shortcuts import render


def homeView():
    return render('home.html')

def usersListView():
    users = User.objects.all()

    context = {
        'users': users
    }
    return render('users_list.html', context)
