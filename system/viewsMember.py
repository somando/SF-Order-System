from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from dotenv import load_dotenv
import datetime

load_dotenv()

# Create your views here.

user_admin = ['soma']
user_ticket = []

for i in user_admin:
    user_ticket.append(i)

@login_required
def member(request):
    username = request.user.username
    if username in user_admin:
        if request.method == 'GET':
            messages = []
            message = forWorkerData.objects.all()
            for i in message:
                messages.append(i)
            return render(request, 'system/member.html', {
                "messages": messages
            })
        elif request.method == 'POST':
            barcode = request.POST['barcode']
            member_data = memberData.objects.all()
            for i in member_data:
                if i.barcode == barcode:
                    member = memberData.objects.get(id = i.id)
                    break
            if member.work == True:
                work = False
                status = '退勤'
            else:
                work = True
                status = '出勤'
            member.work = work
            member.save()
            memberScanData.objects.create(member_id = int(member.id), datetime = datetime.datetime.now(), work = work)
            return render(request, 'system/membersave.html', {
                'member': member,
                'status': status
            })
    else:
        return render(request, 'system/norole.html', {
            "mode": "Member"
        })

@login_required
def memberdetail(request, userid):
    username = request.user.username
    if username in user_admin:
        if request.method == "POST":
            return JsonResponse('Receive POST')
    else:
        return render(request, 'system/norole.html', {
            "mode": "Member"
        })