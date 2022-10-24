import os
from django.contrib.gis.utils import LayerMapping

from GeoTrackApp.settings import BASE_DIR
from .models import County

county_mapping = {
    'objectid': 'OBJECTID',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'county3_field': 'COUNTY3_',
    'county3_id': 'COUNTY3_ID',
    'county': 'COUNTY',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/kenyan-counties','County.shp'))

def run(verbose=True):
    layer = LayerMapping(County, county_shp, county_mapping, transform=False, encoding='iso-8859-1')
    layer.save(strict=True, verbose=verbose)