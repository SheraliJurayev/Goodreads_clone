
from django.urls import path , include
from users.views import RegisterView , LoginView , ProfileView

app_name = 'users'
urlpatterns = [
    path('register/' , RegisterView.as_view() , name='register_page') , 
    path('login/' , LoginView.as_view() , name='login_page') , 
    path('profile/' , ProfileView.as_view() , name='profile_page') , 
]
