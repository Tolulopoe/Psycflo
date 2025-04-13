from django.contrib import admin
from.models import AidRequest
# Register your models here.
admin.site.register(AidRequest)
class MemberAdmin(admin.ModelAdmin):
  list_display = ("brandname",  "donated_at",)
