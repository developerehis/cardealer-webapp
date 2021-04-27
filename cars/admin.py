from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img  src="()" width="40" style="border-radius: 30px;" />'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Car Image'
    list_display = ('thumbnail', 'car_title', 'color', 'model','year', 'body_style', 'is_featured')
    list_display_links =  ('thumbnail', 'car_title',)
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'fuel_type')

admin.site.register(Car, CarAdmin)