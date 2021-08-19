from django.contrib import admin

from house.models import House

class HouseAdmin(admin.ModelAdmin):
  readonly_fields = ('id', 'created_at',)

admin.site.register(House, HouseAdmin)
