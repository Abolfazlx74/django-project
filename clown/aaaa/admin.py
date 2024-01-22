from django.contrib import admin
from .models import dalghak,circus,Genres 
class showAuthor(admin.ModelAdmin):
    list_display = ["ID","FullName","IsAlive"]
    search_fields = ["FullName"]
    actions = ("is_alive", "is_dead") 
    # @admin.action(description="is_alive")
    def is_alive(modeladmin, request, queryset):
        queryset.update(IsAlive=True)
    def is_dead(modeladmin, request, queryset):
        queryset.update(IsAlive=False)
admin.site.register(circus,showAuthor)
admin.site.register(dalghak)
admin.site.register(Genres)