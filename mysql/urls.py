"""
URL configuration for mysql project.

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
from api import views
from rest2 import views as rest2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>', views.student_detail),
    path('studentapi/',views.student_api),

    # path('studentapi2/',rest2.studentapi),
    # path('studentapi2/<int:pk>',rest2.studentapi),

    path('studentapi2/',rest2.studentapi.as_view()),
    path('studentapi2/<int:pk>',rest2.studentapi.as_view()),

    path('modelmixin/',rest2.StudentList.as_view()),
    path('modelmixincreate/',rest2.StudentCreate.as_view()),
    path('modelmixin/<int:pk>/',rest2.StudentRetrive.as_view()),
    path('modelmixinupdate/<int:pk>/',rest2.StudentUpdate.as_view()),
    path('modelmixindelete/<int:pk>/',rest2.StudentDestroy.as_view()),

    path('modelmixinnew/',rest2.StudentLC.as_view()),
    path('modelmixinnew/<int:pk>/',rest2.StudentRUD.as_view()),
]
