from django.contrib import admin

from reporter.models import County, Incidence
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
    
class CountyAdmin(LeafletGeoAdmin):
    list_display = ('county', 'county3_id')
    
admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(County, CountyAdmin)
