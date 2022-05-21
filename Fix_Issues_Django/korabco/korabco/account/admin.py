from django.contrib import admin
from account.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_confirmed', 'created_on', 'updated_on')
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ['user', ]


# Registers the account profile model at the admin backend.
admin.site.register(Profile, ProfileAdmin)