
from django.urls import path , include
from users.views import RegisterView , LoginView

app_name = 'users'
urlpatterns = [
    path('register/' , RegisterView.as_view() , name='register_page') , 
    path('login/' , LoginView.as_view() , name='login_page') , 
]
