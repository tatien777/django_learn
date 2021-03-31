from django.contrib import admin

#models db 
from .models import Student, Place, Restaurant, Waiter, Article, Publication

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','age','address']
admin.site.register(Student,StudentAdmin)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Article)
admin.site.register(Publication)