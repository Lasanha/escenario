from django.contrib import admin
from generator.models import Esc, EscImg


class EscImgAdmin(admin.ModelAdmin):
    """Admin config for EscImg model"""
    raw_id_fields = ['esc']
    readonly_fields = ['criado_em']


class EscAdmin(admin.ModelAdmin):
    """Admin config for Esc model"""
    readonly_fields = ['criado_em']


admin.site.register(EscImg, EscImgAdmin)
admin.site.register(Esc, EscAdmin)
