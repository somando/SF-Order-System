from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *
from dotenv import load_dotenv

load_dotenv()

# Create your views here.

user_admin = ['soma']
user_ticket = []

for i in user_admin:
    user_ticket.append(i)

@login_required
def ticket(request):
    username = request.user.username
    if username in user_ticket:
        if request.method == 'GET':
            messages = []
            message = forWorkerData.objects.all()
            for i in message:
                messages.append(i)
            menus = []
            menu_data = menuData.objects.all()
            for menu in menu_data:
                menus.append(menu)
            return render(request, 'system/ticket.html', {
                "menus": menus
            })
        elif request.method == 'POST':
            barcode = request.POST['barcode']
            return redirect('/ticket/' + barcode)
    else:
        return render(request, 'system/norole.html', {
            "mode": "Ticket"
        })

@login_required
def ticketDetail(request, barcode):
    username = request.user.username
    if username in user_ticket:
        if request.method == 'GET':
            messages = []
            message = forWorkerData.objects.all()
            for i in message:
                messages.append(i)
            ticket_data = ticketData.objects.all()
            for i in ticket_data:
                if i.barcode == barcode:
                    ticket = ticketData.objects.get(id = i.id)
                    break
            menus = []
            menu_data = menuData.objects.all()
            for menu in menu_data:
                menus.append(menu)
            return render(request, 'system/ticketDetail.html', {
                "menus": menus,
                "messages": messages,
                "ticket": ticket,
            })
        elif request.method == 'POST':
            messages = []
            message = forWorkerData.objects.all()
            for i in message:
                messages.append(i)
            menus = []
            menu_data = menuData.objects.all()
            for menu in menu_data:
                menus.append(menu)
            id = int(request.POST['id'])
            ticket = ticketData.objects.get(id = id)
            if ticket.available == False:
                ticket.available = True
                available = "有効化"
            else:
                ticket.available = False
                available = "無効化"
            ticket.save()
            return render(request, 'system/ticketAvailable.html', {
                "messages": messages,
                "menus": menus,
                "ticket": ticket,
                "available": available
            })
    else:
        return render(request, 'system/norole.html', {
            "mode": "Ticket"
        })