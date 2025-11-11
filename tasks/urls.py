from django.urls import path
from . import views

#täällä määritellään kaikki sovelluksen url-polut
#jokainen polku osoittaa tiettyyn näkymäfunktioon, joka käsittelee pyynnön

urlpatterns = [
    #käyttäjän hallinta
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

    #tehtävät
    path('', views.index, name=""),
    path('update-task/<str:pk>/', views.updateTask, name="update-task"),
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),
    path('toggle-complete/<str:pk>/', views.toggleComplete, name='toggle-complete'),

]