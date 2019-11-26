from django.urls import path

from api.views import district_list, district_sub_counties_list, sub_counties_list

urlpatterns = [
    path('districts', district_list),
    path('districts/<int:district_id>/sub-counties', district_sub_counties_list),
    path('sub-counties', sub_counties_list),
]
