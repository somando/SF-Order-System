from django.urls import path
from . import (
    views,
    viewsBackyard,
    viewsOrder,
    viewsRegister,
    viewsAnalytics,
    viewsSettings
)

app_name = 'system'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signin/', views.Login, name='login'),
    path('signout/', views.Logout, name='logout'),
    path('signup/', views.AccountRegistration.as_view(), name='signup'),
    path('backyard/', viewsBackyard.backyard, name='backyard'),
    path('order/', viewsOrder.order, name='order'),
    path('register/', viewsRegister.registerTop, name='register'),
    path('register/<int:id>', viewsRegister.registerTable, name='register'),
    path('register/ticket/', viewsRegister.useTicket, name="useTicket"),
    path('register/discount/', viewsRegister.discount, name="useTicket"),
    path('register/next/', viewsRegister.registerNext, name="useTicket"),
    path('analytics/', viewsAnalytics.analytics, name="analytics"),
    path('analytics/format/', viewsAnalytics.formatAnalytics, name="analyticsSet"),
    path('settings/', viewsSettings.settings, name='settings'),
    path('settings/<slug:menu>/', viewsSettings.setting, name='settings'),
    path('settings/order/edit/<int:id>/', viewsSettings.editOrder, name='addMember'),
    path('settings/order/delete/<int:id>', viewsSettings.deleteOrder, name='addMember'),
    path('settings/menu/add/', viewsSettings.addMenu, name='addMember'),
    path('settings/menu/edit/<int:id>/', viewsSettings.editMenu, name='addMember'),
    path('settings/menu/delete/<int:id>', viewsSettings.deleteMenu, name='addMember'),
    path('settings/table/add/', viewsSettings.addTable, name='addMember'),
    path('settings/table/edit/<int:id>/', viewsSettings.editTable, name='addMember'),
    path('settings/table/delete/<int:id>', viewsSettings.deleteTable, name='addMember'),
    path('settings/ticket/add/', viewsSettings.addTicket, name='addMember'),
    path('settings/ticket/edit/<int:id>/', viewsSettings.editTicket, name='addMember'),
    path('settings/ticket/delete/<int:id>', viewsSettings.deleteTicket, name='addMember'),
    path('settings/message/add/', viewsSettings.addForWorker, name='addMember'),
    path('settings/message/edit/<int:id>/', viewsSettings.editForWorker, name='addMember'),
    path('settings/message/delete/<int:id>', viewsSettings.deleteForWorker, name='addMember'),
    path('settings/analytics/edit/', viewsSettings.analytics, name='settingAnalytics'),
    path('csrf_token/', views.csrf_token, name="csrf_token"),
]
