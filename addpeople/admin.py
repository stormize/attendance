from django.contrib import admin
from .models import people
# Register your models here.
class mypeople(admin.ModelAdmin):
    list_display = ('type','name','attendance','sector','date')
    list_filter = ('date','type','sector')
    search_fields = ('name','type')

admin.site.register(people,mypeople)
