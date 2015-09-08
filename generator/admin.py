from django.contrib import admin
from generator.models import Esc, EscImg


class EscImgAdmin(admin.ModelAdmin):
    raw_id_fields = ['esc']

admin.site.register(EscImg, EscImgAdmin)
admin.site.register(Esc)
