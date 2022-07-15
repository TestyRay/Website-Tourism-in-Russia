from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "mobile_phone",
        "email", "comment", "date",
    )


admin.site.register(Application, ApplicationAdmin)


