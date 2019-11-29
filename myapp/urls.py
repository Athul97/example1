from django.urls import path
from . import views

urlpatterns = [
    path('assign7', views.fn_index1),
    path('fb',views.fn_index2),
    path('fbhome',views.fn_index3),
]
