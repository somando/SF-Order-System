from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *
from dotenv import load_dotenv
import json

load_dotenv()

# Create your views here.

user_admin = ['soma']
user_ticket = []

for i in user_admin:
    user_ticket.append(i)

@login_required
def backyard(request):
    if request.method == "GET":
        messages = []
        message = forWorkerData.objects.all()
        for i in message:
            messages.append(i)
        order_detail = []
        tables = tableData.objects.all()
        for table in tables:
            order_detail.append([table.id, table.name, [], table.message])
        menus = menuData.objects.all()
        orders = orderData.objects.all()
        for order in orders:
            if order.provide == False:
                for detail in order_detail:
                    if order.table_id == detail[0]:
                        for menu in menus:
                            if order.menu_id == menu.id:
                                detail[2].append([order.id, menu.name, order.count])
        return render(request, 'system/backyard.html', {
            "orders": order_detail,
            "messages": messages
        })
    elif request.method == "POST":
        post_data = json.loads(request.body.decode())
        id = post_data.get('id')
        order = orderData.objects.get(id = id)
        order.provide = True
        order.save()
        return redirect('/backyard/')