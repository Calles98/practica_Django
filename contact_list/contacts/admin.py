from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    prepopulated_fields = {'slug':('first_name', 'last_name')}

# Register your models here.
admin.site.register(Contact, ContactAdmin)