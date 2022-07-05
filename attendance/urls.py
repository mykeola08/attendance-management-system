from django.urls import path
from .views import attend_view
from django.contrib.auth import views
from .views import register, HomeView


urlpatterns = [
     path('', HomeView.as_view(), name='home'),
     path('attendance/', attend_view, name="attend_view"),
     path('register/', register, name="register"),
     path('login/', views.LoginView.as_view(template_name="templates/users/login.html"), name="login"),
     path('logout/', views.LogoutView.as_view(template_name="templates/users/logout.html"), name="logout"),

]
