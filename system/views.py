from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token

# Create your views here.

def csrf_token(request):
    return JsonResponse({"token": get_token(request)})

def backyard(request):
    return render(request, 'system/backyard.html')