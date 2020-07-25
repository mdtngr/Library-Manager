from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import UserData

# Register your models here.

class MyUserAdmin(UserAdmin):
    model = UserData
    list_display            = ('email', 'first_name', 'year_of_joining', 'last_login', 'is_admin', 'is_staff')
    search_fields           = ('email', 'first_name',)
    readonly_fields         = ('last_login',)
    filter_horizontal       =()
    list_filter             =()
    fieldsets               =()
admin.site.register(UserData, MyUserAdmin)