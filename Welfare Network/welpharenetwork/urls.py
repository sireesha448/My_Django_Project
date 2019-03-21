"""welpharenetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView

from cewn import views
from cewn.models import AcceptedUsers
from cewn.models import RejectedUser
from cewn.models import ApprovalUsers
from cewn.models import Thoughts
from cewn.models import Events
from cewn.models import Technical
from cewn.models import WorkExperience
from cewn.models import Property
from cewn.models import ShareMarket
from cewn.models import Reference
from cewn.models import Matrimonial
from cewn.models import Celebrations
from cewn.models import Travel




urlpatterns = [
    #admin pag url's
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="login.html"),name='index'),
    path('newuser/',views.RegisterNewUser.as_view()),
    path('login/',views.LoginCheck.as_view()),
    path('viewapprovalusers/',ListView.as_view(template_name="Adminview/viewapprovalusers.html",model=ApprovalUsers)),
    path('accept/',views.Accept.as_view()),
    path('reject/',views.Reject.as_view()),
    path('viewacceptedusers/',ListView.as_view(model=AcceptedUsers,template_name="Adminview/viewacceptedusers.html")),
    path('viewrejectedusers/',ListView.as_view(model=RejectedUser,template_name="Adminview/viewrejectedusers.html")),
    path('viewuserthoughts/',ListView.as_view(template_name="Adminview/viewuserthoughts.html",model=Thoughts)),
    path('viewuserevents/',ListView.as_view(template_name="Adminview/viewuserevents.html",model=Events)),
    path('viewusertechnical/',ListView.as_view(template_name="Adminview/viewusertechnical.html",model=Technical)),
    path('viewuserworkexperience/',ListView.as_view(template_name="Adminview/viewuserworkexperience.html",model=WorkExperience)),
    path('viewuserproperty/',ListView.as_view(template_name="Adminview/viewuserproperty.html",model=Property)),
    path('viewusersharemarket/',ListView.as_view(template_name="Adminview/viewusersharemarket.html",model=ShareMarket)),
    path('viewusermatrimonial/',ListView.as_view(template_name="Adminview/viewusermatrimonial.html",model=Matrimonial)),
    path('viewusercelebrations/',ListView.as_view(template_name="Adminview/viewusercelebrations.html",model=Celebrations)),
    path('viewusertravel/',ListView.as_view(template_name="Adminview/viewusertravel.html",model=Travel)),
    path('viewuserreferences/',ListView.as_view(template_name="Adminview/viewuserreferences.html",model=Reference)),
    #user page url's
    path('addthoughts/',views.AddThoughts.as_view()),
    path('usermenu/',TemplateView.as_view(template_name="Userview/usermenu.html")),
    path('viewthoughts/',ListView.as_view(model=Thoughts,template_name="Userview/viewthought.html")),
    path('addevents/',views.AddEvents.as_view()),
    path('viewevents/',ListView.as_view(model=Events,template_name="Userview/viewevent.html")),
    path('addtechnical/',views.AddTechnical.as_view()),
    path('viewtechnical/',ListView.as_view(template_name="Userview/viewtechnical.html",model=Technical)),
    path('addworkexperience/',views.AddWorkExperience.as_view()),
    path('viewworkexperience/',ListView.as_view(template_name="Userview/viewworkexperience.html",model=WorkExperience)),
    path('addproperty/',views.AddProperty.as_view()),
    path('viewproperty/',ListView.as_view(template_name="Userview/viewproperty.html",model=Property)),
    path('addsharemarket/',views.AddShareMarket.as_view()),
    path('viewsharemarket/',ListView.as_view(model=ShareMarket,template_name="Userview/viewsharemarket.html")),
    path('addreference/',views.AddReference.as_view()),
    path('viewreference/',ListView.as_view(template_name="Userview/viewreference.html",model=Reference)),
    path('addmatrimonial/',views.AddMatrimonial.as_view()),
    path('viewmatrimonial/',ListView.as_view(template_name="Userview/viewmatrimonial.html",model=Matrimonial)),
    path('addcelebrations/',views.AddCelebrations.as_view()),
    path('viewcelebrations/',ListView.as_view(template_name="Userview/viewcelebrations.html",model=Celebrations)),
    path('addtravel/',views.AddTravel.as_view()),
    path('viewtravel/',ListView.as_view(template_name="Userview/viewtravel.html",model=Travel))
 ]
