from django.contrib import admin
from phonebook.models import phonebooks

# Register your models here.
class PhoneBookView(admin.ModelAdmin):
    list_display = ('id', 'name', 'pnum', 'email', 'addr', 'birth')


admin.site.register(phonebooks, PhoneBookView)
