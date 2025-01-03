"""sandbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sandboxapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("inReg", views.inReg),
    path("sfReg", views.sfReg),
    path("login/", views.login),
    path("adminHome", views.adminHome),
    path("inHome", views.inHome),
    path("inProfile", views.inProfile),
    path("inViewIdea", views.inViewIdea),
    path("inViewSf", views.inViewSf),
    path("inChangeImage", views.inChangeImage),
    path("inShowInterest", views.inShowInterest),
    path("inViewInvestmentOffers", views.inViewInvestmentOffers),
    path("inMakePayment", views.inMakePayment),
    path("inViewPayments", views.inViewPayments),
    path("inChat", views.inChat),
    path("sfHome", views.sfHome),
    path("sfProfile", views.sfProfile),
    path("sfChangeImage", views.sfChangeImage),
    path("sfPost", views.sfPost),
    path("sfViewSelfPost", views.sfViewSelfPost),
    path("sfUpdateIdea", views.sfUpdateIdea),
    path("sfDeleteIdea", views.sfDeleteIdea),
    path("sfViewIdea", views.sfViewIdea),
    path("sfViewSf", views.sfViewSf),
    path("sfViewInvestemntOffers", views.sfViewInvestemntOffers),
    path("sfOnInvestmentOffer", views.sfOnInvestmentOffer),
    path("sfViewPayments", views.sfViewPayments),
    path("sfAddFeedBack", views.sfAddFeedBack),
    path("sfChat", views.sfChat),
    path("sfChatPer", views.sfChatPer),
    path("adminInvestor", views.adminInvestor),
    path("approveInvestors", views.approveInvestors),
    path("adminStartUp", views.adminStartUp),
    path("approveStartUp", views.approveStartUp),
    path("adminViewFeedback", views.adminViewFeedback),
    path("addWorkSpace", views.addWorkSpace),
    path("updateWorkSpace", views.updateWorkSpace),
    path("deleteWorkSpace", views.deleteWorkSpace),
    path("workSpaces", views.workSpaces),
    path("bookWorkSpace", views.bookWorkSpace),
    path("viewBookings", views.viewBookings),
    path("adminviewBookings", views.adminviewBookings),
]
