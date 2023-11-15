from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *

user_admin = ['soma']

@login_required
def analytics(request):
    username = request.user.username
    if username in user_admin:
        messages = []
        message = forWorkerData.objects.all()
        for i in message:
            messages.append(i)
        analytics = analyticsData.objects.all()
        for i in analytics:
            id = i.id
            break
        analytics = analyticsData.objects.get(id = id)
        price = analytics.price
        discount = analytics.discount
        order = orderData.objects.all()
        order_count = 0
        for i in order:
            order_count += 1
        ticket_count = 0
        ticket = ticketData.objects.all()
        for i in ticket:
            if i.used == True:
                ticket_count += 1
        return render(request, 'system/analytics.html', {
            "messages": messages,
            "price": price,
            "order": order_count,
            "ticket": ticket_count,
            "discount": discount,
        })
    else:
        return render(request, 'system/norole.html', {
            "mode": "Analytics"
        })

def formatAnalytics(request):
    analyticsData.objects.create(price = 0, discount = 0)
    return HttpResponse("Success")