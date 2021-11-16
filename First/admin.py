from django.contrib import admin
from .models import Flight,Comment,status
from django.contrib.auth.admin import UserAdmin

class statusInline(admin.StackedInline):
    model = status 
    can_delete = False


class ExtendedProfileAdmin(UserAdmin):
    inlines = (statusInline,)

admin.site.register(Flight)

admin.site.register(Comment)
