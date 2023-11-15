from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from dotenv import load_dotenv
import datetime
from dateutil import tz

load_dotenv()

# Create your views here.

user_admin = ['soma']

@login_required
def shift(request):
    now = datetime.datetime.now()
    username = request.user.username
    if username in user_admin:
        if request.method == 'GET':
            messages = []
            message = forWorkerData.objects.all()
            for i in message:
                messages.append(i)
            now_shifts = []
            after_shifts = []
            shift_data = shiftData.objects.all()
            for i in shift_data:
                print(type(i.start))
                if i.start <= now and now <= i.finish:
                    now_shifts.append(i)
                elif now <= i.start:
                    after_shifts.append(i)
            return render(request, 'system/shift.html', {
                "messages": messages,
                "now_shifts": now_shifts,
            })
    else:
        return render(request, 'system/norole.html', {
            "mode": "Shift"
        })