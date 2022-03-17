from django.contrib import admin

# Register your models here.
from .models import Contact,Newsletter,Gallery,Events,Home
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message','is_active','created_at')
    list_filter = ('is_active', 'created_at')
admin.site.register(Contact,ContactAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    
admin.site.register(Newsletter,NewsletterAdmin)  
admin.site.register(Gallery)
admin.site.register(Events)
admin.site.register(Home)