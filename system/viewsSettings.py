from django.shortcuts import render
from django.shortcuts import redirect
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
def editOrder(request, id):
    username = request.user.username
    if username in user_admin:
        order = orderData.objects.get(id = id)
        if request.method == "GET":
            arr = ["", "", "", False, False, False]
            arr[0] = order.table_id
            arr[1] = order.menu_id
            arr[2] = order.count
            arr[3] = order.provide
            arr[4] = order.checkout
            arr[5] = order.next
            tables = []
            table = tableData.objects.all()
            for i in table:
                tables.append(i)
            menus = []
            menu = menuData.objects.all()
            for i in menu:
                menus.append(i)
            return render(request, 'system/addOrder.html', {
                "arr": arr,
                "tables": tables,
                "menus": menus,
                "method": "Update"
            })
        else:
            order.table_id = request.POST['table']
            order.menu_id = request.POST['menu']
            order.count = request.POST['number']
            provide = request.POST['provide']
            checkout = request.POST['checkout']
            next = request.POST['next']
            if provide == 'provide':
                provide = True
            else:
                provide = False
            order.provide = provide
            if checkout == 'checkout':
                checkout = True
            else:
                checkout = False
            order.checkout = checkout
            if next == 'next':
                next = True
            else:
                next = False
            order.next = next
            order.save()
            return redirect('/settings/order/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def deleteOrder(request, id):
    username = request.user.username
    if username in user_admin:
        member = orderData.objects.get(id = id)
        member.delete()
        return redirect('/settings/order/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def addMenu(request):
    username = request.user.username
    if username in user_admin:
        if request.method == "GET":
            arr = ["", "", "0", False]
            return render(request, 'system/addMenu.html', {
                "arr": arr,
                "method": "Create"
            })
        else:
            name = request.POST['name']
            price = request.POST['price']
            count = request.POST['count']
            soldout = request.POST['soldout']
            if soldout == "soldout":
                soldout = True
            else:
                soldout = False
            menuData.objects.create(name = name, price = int(price), count = int(count), soldout = soldout)
            return redirect('/settings/menu/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def editMenu(request, id):
    username = request.user.username
    if username in user_admin:
        menu = menuData.objects.get(id = id)
        if request.method == "GET":
            arr = ["", "", "", False]
            arr[0] = menu.name
            arr[1] = menu.price
            arr[2] = menu.count
            arr[3] = menu.soldout
            return render(request, 'system/addMenu.html', {
                "arr": arr,
                "method": "Update"
            })
        else:
            menu.name = request.POST['name']
            menu.price = request.POST['price']
            menu.count = request.POST['count']
            soldout = request.POST['soldout']
            if soldout == "soldout":
                soldout = True
            else:
                soldout = False
            menu.soldout = soldout
            menu.save()
            return redirect('/settings/menu/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def deleteMenu(request, id):
    username = request.user.username
    if username in user_admin:
        menu = menuData.objects.get(id = id)
        menu.delete()
        return redirect('/settings/menu/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def addTable(request):
    username = request.user.username
    if username in user_admin:
        if request.method == "GET":
            arr = ['', '', '', 0, 0]
            return render(request, 'system/addTable.html', {
                "arr": arr,
                "method": "Create"
            })
        else:
            name = request.POST['name']
            use = request.POST['use']
            if use == "using":
                use = True
            else:
                use = False
            message = request.POST['message']
            if message == "":
                message = "None"
            ticket = int(request.POST['ticket'])
            discount = int(request.POST['discount'])
            tableData.objects.create(name = name, use = use, message = message, ticket_price = ticket, discount = discount)
            return redirect('/settings/table/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def editTable(request, id):
    username = request.user.username
    if username in user_admin:
        table = tableData.objects.get(id = id)
        if request.method == "GET":
            arr = [table.name, table.use, table.message, table.ticket_price, table.discount]
            return render(request, 'system/addTable.html', {
                "arr": arr,
                "method": "Update"
            })
        else:
            table.name = request.POST['name']
            use = request.POST['use']
            table.message = request.POST['message']
            table.ticket_price = request.POST['ticket']
            table.discount = request.POST['discount']
            if use == "using":
                use = True
            else:
                use = False
            table.use = use
            table.save()
            return redirect('/settings/table/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def deleteTable(request, id):
    username = request.user.username
    if username in user_admin:
        table = tableData.objects.get(id = id)
        table.delete()
        return redirect('/settings/table/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def addTicket(request):
    username = request.user.username
    if username in user_admin:
        if request.method == "GET":
            tickets = []
            ticket = ticketData.objects.all()
            for i in ticket:
                tickets.append(i)
            arr = []
            menus = []
            menu = menuData.objects.all()
            for i in menu:
                menus.append(i)
            return render(request, 'system/addTicket.html', {
                "arr": arr,
                "tickets": tickets,
                "menus": menus,
                "method": "Create"
            })
        else:
            menu = request.POST['menu']
            barcode = request.POST['barcode']
            available = request.POST['available']
            numstart = int(request.POST['numstart'])
            numfinish = int(request.POST['numfinish'])
            tickets = ticketData.objects.all()
            for i in range(numstart, numfinish + 1):
                unique = True
                for ticket in tickets:
                    if ticket.barcode == barcode:
                        unique = False
                if available == 'available':
                    availableTF = True
                else:
                    availableTF = False
                used = request.POST['used']
                if used == 'used':
                    used = True
                else:
                    used = False
                if unique == True:
                    ticketData.objects.create(menu_id = menu, barcode = barcode + str(i).zfill(3), available = availableTF, used = used)
                else:
                    return render(request, 'system/ticketFail.html')
            return redirect('/settings/ticket/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def editTicket(request, id):
    username = request.user.username
    if username in user_admin:
        ticket = ticketData.objects.get(id = id)
        if request.method == "GET":
            arr = ["", "", False, False]
            arr[0] = ticket.menu_id
            arr[1] = ticket.barcode
            arr[2] = ticket.available
            arr[3] = ticket.used
            menus = []
            menu = menuData.objects.all()
            for i in menu:
                menus.append(i)
            return render(request, 'system/addTicket.html', {
                "arr": arr,
                "menus": menus,
                "method": "Update"
            })
        else:
            ticket.menu_id = request.POST['menu']
            ticket.barcode = request.POST['barcode']
            available = request.POST['available']
            if available == 'available':
                available = True
            else:
                available = False
            ticket.available = available
            used = request.POST['used']
            if used == 'used':
                used = True
            else:
                used = False
            ticket.used = used
            ticket.save()
            return redirect('/settings/ticket/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def deleteTicket(request, id):
    username = request.user.username
    if username in user_admin:
        ticket = ticketData.objects.get(id = id)
        ticket.delete()
        return redirect('/settings/ticket/')
    else:
        return render(request, 'system/noroleSetting.html')

@login_required
def addForWorker(request):
    if request.method == "GET":
        arr = []
        return render(request, 'system/addMessage.html', {
            "arr": arr,
            "method": "Create"
        })
    else:
        priority = request.POST['priority']
        message = request.POST['message']
        forWorkerData.objects.create(priority = priority, message = message)
        return redirect('/settings/message/')

@login_required
def editForWorker(request, id):
    message = forWorkerData.objects.get(id = id)
    if request.method == "GET":
        arr = [message.priority, message.message]
        return render(request, 'system/addMessage.html', {
            "arr": arr,
            "method": "Update"
        })
    else:
        message.message = request.POST['message']
        message.priority = request.POST['priority']
        message.save()
        return redirect('/settings/message/')

@login_required
def deleteForWorker(request, id):
    message = forWorkerData.objects.get(id = id)
    message.delete()
    return redirect('/settings/message/')

@login_required
def settings(request):
    return redirect('/settings/message/')

@login_required
def setting(request, menu):
    if menu == 'message':
        messages = []
        message = forWorkerData.objects.all()
        for i in message:
            messages.append(i)
        messages.sort(key=lambda item:item.id)
        return render(request, 'system/setforworker.html', {
            "messages": messages
        })
    username = request.user.username
    if username in user_admin:
        if menu == 'order':
            order_data = []
            orders = orderData.objects.all()
            for order in orders:
                order_data.append(order)
            order_data.sort(key=lambda item:item.id)
            tables = []
            table = tableData.objects.all()
            for i in table:
                tables.append(i)
            menus = []
            menu = menuData.objects.all()
            for i in menu:
                menus.append(i)
            return render(request, 'system/setorder.html', {
                "order_data": order_data,
                "tables": tables,
                "menus": menus
            })
        elif menu == 'menu':
            menu_data = []
            menus = menuData.objects.all()
            for menu in menus:
                menu_data.append(menu)
            menu_data.sort(key=lambda item:item.id)
            return render(request, 'system/setmenu.html', {
                "menu_data": menu_data
            })
        elif menu == 'table':
            table_data = []
            tables = tableData.objects.all()
            for table in tables:
                table_data.append(table)
            table_data.sort(key=lambda item:item.id)
            return render(request, 'system/settable.html', {
                "table_data": table_data,
            })
        elif menu == 'ticket':
            menus = []
            menu = menuData.objects.all()
            for i in menu:
                menus.append(i)
            ticket_data = []
            tickets = ticketData.objects.all()
            for ticket in tickets:
                ticket_data.append(ticket)
            ticket_data.sort(key=lambda item:item.id)
            return render(request, 'system/setticket.html', {
                "ticket_data": ticket_data,
                "menus": menus
            })
    else:
        return render(request, 'system/noroleSetting.html')