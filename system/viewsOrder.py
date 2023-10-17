from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from dotenv import load_dotenv
import os
import datetime
import requests

load_dotenv()

# Create your views here.

user_admin = ['soma']
user_ticket = []

for i in user_admin:
    user_ticket.append(i)

@login_required
def order(request):
    menus = []
    menu = menuData.objects.all()
    for i in menu:
        menus.append(i)
    menus.sort(key=lambda item:item.id)
    tables = []
    table = tableData.objects.all()
    for i in table:
        tables.append(i)
    tables.sort(key=lambda item:item.id)
    if request.method == "GET":
        messages = []
        message = forWorkerData.objects.all()
        for i in message:
            messages.append(i)
        orders = []
        order_data = orderData.objects.all()
        for order in order_data:
            orders.append(order)
        orders.sort(key=lambda item:item.id)
        return render(request, 'system/order.html', {
            "orders": orders,
            "tables": tables,
            "menus": menus,
            "messages": messages
        })
    elif request.method == "POST":
        now_time = datetime.datetime.now()
        order_data = []
        soldout = []
        table_id = int(request.POST['table'])
        for table in tables:
            if table.id == table_id:
                table_name = table.name
        for menu in menus:
            count = int(request.POST[str(menu.id)])
            if count > 0:
                order = [menu.name, count]
                menu_id = menu.id
                if menu.soldout:
                    soldout.append(menu.name)
                else:
                    every_menu = menuData.objects.get(id = menu.id)
                    every_menu.count += count
                    every_menu.save()
                    orderData.objects.create(order_time = now_time, table_id = table_id, menu_id = menu_id, count = count, provide = False, checkout = False, next = False)
                    order_data.append(order)
        table = tableData.objects.get(id = table_id)
        table.use = True
        message = request.POST['message']
        if message == "":
            message = "None"
        table.message = message
        table.save()
        if len(order_data) > 0:
            line_message = '\n新規オーダーを受け付けました。\nBackyardページをリロードしてください。'
            lineNotify(line_message)
        return render(request, 'system/ordered.html', {
            "order_data": order_data,
            "now_time": now_time,
            "table_name": table_name,
            "message": message,
            "soldout": soldout,
        })

def lineNotify(message):
    token = os.environ['LINE_NOTIFY_TOKEN']
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': message}
    requests.post(url, headers = headers, data = data)