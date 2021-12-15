from django.contrib import admin

from computers.models import PC, Display


class PCAdmin(admin.ModelAdmin):
    pass


class DisplayAdmin(admin.ModelAdmin):
    pass


admin.site.register(PC, PCAdmin)
admin.site.register(Display, DisplayAdmin)
