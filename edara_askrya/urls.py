from django.urls import path,include
from. import views
urlpatterns = [
    path('',views.dashboard),
    path('/done',views.edara_line),
    path('dashboard',views.dashboard),
]
