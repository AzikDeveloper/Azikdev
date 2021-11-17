from app.views import *

url_patterns = {
    '/': homeView,
    '/hello': helloView,
    '/users': usersListView,
    '/login': loginView,
}
