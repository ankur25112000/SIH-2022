from csv import list_dialects
from django.contrib import admin

# Register your models here.
from chat.models import Chat
from chat.models import Contact


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('message', 'created', 'user',)
    search_fields = ['message']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','mail','subject','message')