from django.contrib import admin
from generator.models import Esc, EscImg


class EscImgAdmin(admin.ModelAdmin):
    raw_id_fields = ['esc']
    readonly_fields = ['criado_em']


class EscAdmin(admin.ModelAdmin):
    readonly_fields = ['criado_em']


admin.site.register(EscImg, EscImgAdmin)
admin.site.register(Esc, EscAdmin)
