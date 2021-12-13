from django.contrib import admin

from computers.models import PCMark, PCModel


class PCMarkAdmin(admin.ModelAdmin):
    pass


class PCModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(PCMark, PCMarkAdmin)
admin.site.register(PCModel, PCModelAdmin)
