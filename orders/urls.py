from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list,name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('report/', views.report_view, name='report'),
    path('report_filter/', views.report_view_form, name='report_view'),
]
