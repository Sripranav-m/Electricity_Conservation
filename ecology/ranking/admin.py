from django.contrib import admin

from .models import ranking,query

admin.site.register(ranking)
admin.site.register(query)

admin.site.site_header = "SRIPRANAV MANNEPALLI"
admin.site.index_title = "RANKING SYSTEM"
