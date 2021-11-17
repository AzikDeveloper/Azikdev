from app.my_models import User
from aziktools.shortcuts import render


def homeView():
    context = {
        'name': 'Done?',
        'users': ['Azizbek', 'R*******']
    }
    return render('home.html', context)


def helloView():
    return 'hi'


def usersListView():
    users = User.objects.all()

    context = {
        'users': users
    }
    return render('users_list.html', context)


def loginView():
    return render('login.html')
