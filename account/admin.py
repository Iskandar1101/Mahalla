from django.contrib import admin
from .models import Region, MahhalaFY, User

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

# Register your models here.


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_quarters', ]

    def get_quarters(self, instance):
        return [quarter.quarter_name for quarter in instance.mahhalafy_set.all()]

    get_quarters.short_description = "Mahalla"


# class QuarterSecurityAdmin(admin.ModelAdmin):
#     list_display = ['id', 'get_posbon']



class MahallaAdmin(admin.ModelAdmin):
    list_display = ('quarter_name', 'region_id', 'staff_member',)
    list_display_links = ('quarter_name',)

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class PosbonAdmin(UserAdmin):
    form = MyUserChangeForm
    list_display = ['username', 'region']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Region', {'fields': ('region',)}),)

admin.site.register(Region, RegionAdmin)
admin.site.register(MahhalaFY, MahallaAdmin)
admin.site.register(User, PosbonAdmin)