from django.contrib import admin

# Register your models here.
from .models import house


class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(House, HouseAdmin)
