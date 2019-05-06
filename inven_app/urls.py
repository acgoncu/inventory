from django.urls import path

from . import views

#simple tutorial
from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('', views.index, name='index'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('purchaserequest/new/', views.purchase_request_new, name='purchase_request_new'),
#    path('purchaserequest/<int:pk>/', views.purchase_request_detail, name='purchase_request_detail'),
    path('purchase_list/', views.purchase_list, name='purchase_list' ),
]