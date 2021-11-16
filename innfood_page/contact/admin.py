from contact.models import Contact
from django.contrib import admin

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('procedure','name', 'mail', 'phone', 'message', 'created')
    list_filter = ('procedure', 'status')
    list_display = ('name','procedure', 'status')

admin.site.register(Contact, ContactAdmin)


    

