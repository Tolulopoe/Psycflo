from django.contrib import admin
from.models import Aid
# Register your models here.
admin.site.register(Aid)
class MemberAdmin(admin.ModelAdmin):
  list_display = ("brandname",  "donated_at",)


