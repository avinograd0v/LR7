from django.contrib import admin
from .models import *
# Register your models here.

class AnteAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount')
    search_fields = ('id', 'amount')

admin.site.register(ante_model, AnteAdmin)

class TeamAdmin(admin.ModelAdmin):
    def win_pro(self, obj):
        p=obj.quantity_win/(obj.quantity_win+obj.quantity_lose)
        return '%.2f' % p
    list_display = ('id', 'name', 'kind_of_sport','rating','quantity_win','quantity_lose','win_pro')
    list_filter = ['rating']
    search_fields = ('id', 'name')

admin.site.register(team_model, TeamAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')

admin.site.register(User, UserAdmin)