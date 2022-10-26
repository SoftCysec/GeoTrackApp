from .views import HomePageView, county_datasets
from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('county_data/', county_datasets, name='county'),
    # path('Incidencs_data/', HomePageView.as_view(), name='incidence'),
    
]
