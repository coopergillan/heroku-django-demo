from django.contrib import admin

from hello.models import Greeting

# Register your models here.

class GreetingAdmin(admin.ModelAdmin):
    list_display = ('when', 'noun')
    list_filter = ('noun', )
    search_fields = ('noun', )

admin.site.register(Greeting, GreetingAdmin)
