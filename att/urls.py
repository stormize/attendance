
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addpeople/',include('addpeople.urls')),
    path('edara_askrya', include('edara_askrya.urls')),
    path('shon_kanonya', include('shon_kanonya.urls')),
    path('takhtit', include('takhtit.urls')),
    path('tanzim', include('tanzim.urls')),
    path('afrad', include('afrad.urls')),
    path('edara_mahlya', include('edara_mahlya.urls')),
    path('shon_shakhsya', include('shon_shakhsya.urls')),
    path('taabaa', include('taabaa.urls')),
]
urlpatterns += staticfiles_urlpatterns()
