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
def registerTop(request):
    username = request.user.username
    if username in user_admin:
        messages = []
        message = forWorkerData.objects.all()
        for i in message:
            messages.append(i)
        tables = []
        table = tableData.objects.all()
        for i in table:
            tables.append(i)
        tables.sort(key=lambda item:item.id)
        return render(request, 'system/registerTop.html', {
            "messages": messages,
            "tables": tables
        })
    else:
        return render(request, 'system/norole.html', {
            "mode": "Register"
        })

@login_required
def registerTable(request, id):
    username = request.user.username
    if username in user_admin:
        if request.method == 'GET':
            price = 0
            messages = []
            message = forWorkerData.objects.all()
            for i in message:
                messages.append(i)
            menus = []
            menu = menuData.objects.all()
            for i in menu:
                menus.append(i)
            tables = []
            table = tableData.objects.all()
            for i in table:
                tables.append(i)
            tables.sort(key=lambda item:item.id)
            table = tableData.objects.get(id = id)
            orders = []
            order_data = orderData.objects.all()
            for order in order_data:
                if order.table_id == id and order.checkout == False and order.next == False and order.provide == True:
                    for i in menu:
                        if i.id == order.menu_id:
                            orders.append([order.id, i.name, order.count, i.price * order.count])
                            price += i.price * order.count
            discount = table.ticket_price + table.discount
            price -= discount
            return render(request, 'system/registerTable.html', {
                "messages": messages,
                "menus": menus,
                "tables": tables,
                "select": table,
                "orders": orders,
                "discount": discount,
                "price": price
            })
        elif request.method == 'POST':
            tableid = int(request.POST['table'])
            orders = orderData.objects.all()
            use = False
            for i in orders:
                if i.table_id == tableid:
                    order = orderData.objects.get(id = i.id)
                    if order.next == False and i.provide == True:
                        order.checkout = True
                    else:
                        use = True
                        order.next = False
                    order.save()
            table = tableData.objects.get(id = tableid)
            table.use = use
            table.ticket_price = 0
            table.discount = 0
            table.save()
            return render(request, 'system/thankyou.html')
    else:
        return render(request, 'system/norole.html', {
            "mode": "Register"
        })

@login_required
def useTicket(request):
    username = request.user.username
    if username in user_admin:
        if request.method == 'POST':
            id = None
            tableid = request.POST['table']
            code = request.POST['barcode']
            ticket_data = ticketData.objects.all()
            for ticket in ticket_data:
                if ticket.barcode == code:
                    id = ticket.id
            if id != None:
                ticket = ticketData.objects.get(id = id)
                if ticket.available == True and ticket.used == False:
                    ticket.used = True
                    table = tableData.objects.get(id = tableid)
                    menu = menuData.objects.get(id = ticket.menu_id)
                    table.ticket_price += menu.price
                    table.save()
                    ticket.save()
            return redirect('/register/' + tableid)
    else:
        return render(request, 'system/norole.html', {
            "mode": "Register"
        })

@login_required
def discount(request):
    username = request.user.username
    if username in user_admin:
        if request.method == 'POST':
            tableid = request.POST['table']
            discount = request.POST['discountPrice']
            table = tableData.objects.get(id = tableid)
            table.discount += int(discount)
            table.save()
            return redirect('/register/' + tableid)
    else:
        return render(request, 'system/norole.html', {
            "mode": "Register"
        })

@login_required
def registerNext(request):
    username = request.user.username
    if username in user_admin:
        if request.method == 'POST':
            tableid = request.POST['table']
            next = request.POST.getlist('next[]')
            for i in next:
                order = orderData.objects.get(id = i)
                order.next = True
                order.save()
            return redirect('/register/' + tableid)
    else:
        return render(request, 'system/norole.html', {
            "mode": "Register"
        })