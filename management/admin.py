from django.contrib import admin

from management.models import Position


# Register your models here.
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
