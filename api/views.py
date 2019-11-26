from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import District, SubCounty
from api.serializers import DistrictSerializer, SubCountySerializer


@csrf_exempt
def district_list(request):
    """
    List all districts.
    """
    if request.method == 'GET':
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def district_sub_counties_list(request, district_id):
    """
    List all district sub counties.
    """
    if request.method == 'GET':
        sub_counties = SubCounty.objects.filter(district_id=district_id)
        serializer = SubCountySerializer(sub_counties, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def sub_counties_list(request):
    """
    List all sub counties.
    """
    if request.method == 'GET':
        sub_counties = SubCounty.objects.all()
        serializer = SubCountySerializer(sub_counties, many=True)
        return JsonResponse(serializer.data, safe=False)
