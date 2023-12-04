"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from work.views import EmpView,bookview,itemview,booklist,bookdetail#mobileview,mobilelist,getmobile
from work.views import studentview,getstud,studentlist,studdelete,delbook
urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/',EmpView.as_view()),
    path('book/',bookview.as_view()),
    path('item/',itemview.as_view()),
    path('books/all',booklist.as_view(),name='book-l'),
    path("books/<int:pk>",bookdetail.as_view(),name='book-det'),
    path("books/<int:pk>/remove",delbook.as_view(),name='book-del'),
    # path('mobile/',mobileview.as_view()),
    # path('mobl/',mobilelist.as_view()),
    # path('mob/<int:id>',getmobile.as_view()),
    path('stud/',studentview.as_view()),
    path('studl/',studentlist.as_view(),name='stud-l'),
    path('get/<int:one>',getstud.as_view(),name='stud'),
    path('studd/<int:pk>/remove',studdelete.as_view(),name='stud-del')
]
