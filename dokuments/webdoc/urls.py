from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('document/<int:document_id>/', views.documentmain, name='document'),
    path('document/<int:document_id>/addcomment/', views.addcomment, name='addcomment'),
    path('page/<int:document_id>/<int:page_num>/', views.page, name='page'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('info/', views.info, name='info'),
    path('contacts/', views.contacts, name='contacts'),
    path('payment/', views.payment, name='payment'),
    path('makepayment/', views.makepayment, name='makepayment'),
    path('addresses/', views.addresses, name='addresses'),
    path('makeaddress/', views.makeaddress, name='makeaddress'),
]
