from django.urls import path,include
from. import views
urlpatterns = [
    path('',views.login,name='login'),
    path('add',views.index,name='add'),
    path('done',views.takhtit_line),
    path('dashboard',views.dashboard),

]
