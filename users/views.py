from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.models import User
from users.forms import UserCreateForm
# Create your views here.

class RegisterView(View):
    def get(self, request):

        create_form = UserCreateForm()
        context = {
            'form': create_form
        }
        return render(request, 'users/register.html' , context)
    
    def  post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            username = request.POST['username']
            firstname = request.POST['first_name']
            last_name = request.POST['last_name']    
            email = request.POST['email'] 
            password = request.POST['password']

            user = User.objects.get(
                username=username ,
                firstname=firstname ,
                last_name=last_name , 
                email=email,
                password=password
            )
            user.set_password(password)
            user.save() 

            return redirect('users:login_page')
    
        else:
            context = {
            'form': create_form
            }
            return render(request, 'users/register.html' , context)
    
    

class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')    
    
