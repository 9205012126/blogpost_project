
from django.urls import path

from . import views

urlpatterns = [

    path('',views.allblog , name = 'home'),
path('<int:blog_id>/',views.detail, name = 'detail')
]
