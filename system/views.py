from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import *
from .forms import AccountForm
from dotenv import load_dotenv

load_dotenv()

# Create your views here.

user_admin = ['soma']
user_ticket = []

for i in user_admin:
    user_ticket.append(i)

class AccountRegistration(TemplateView):
    def __init__(self):
        self.params = {
            "AccountCreate": False,
            "account_form": AccountForm(),
        }
    def get(self, request):
        self.params["account_form"] = AccountForm()
        self.params["AccountCreate"] = False
        return render(request, "system/signup.html", context = self.params)
    def post(self, request):
        self.params["account_form"] = AccountForm(data = request.POST)
        if self.params["account_form"].is_valid():
            account = self.params["account_form"].save()
            account.set_password(account.password)
            account.save()
            self.params["AccountCreate"] = True
        else:
            print(self.params["account_form"].errors)
        return render(request, "system/signup.html", context = self.params)

def csrf_token(request):
    return JsonResponse({"token": get_token(request)})

def welcome(request):
    return render(request, 'system/welcome.html')

def Login(request):
    if request.method == 'GET':
        messages = []
        message = forWorkerData.objects.all()
        for i in message:
            messages.append(i)
        return render(request, 'system/login.html', {
            "messages": messages,
        })
    elif request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['password']
        user = authenticate(username = userid, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'system/loginFailed.html')
            else:
                return render(request, 'system/loginFailed.html')
        else:
            return render(request, 'system/loginFailed.html')

@login_required
def Logout(request):
    logout(request)
    return render(request, 'system/signout.html')