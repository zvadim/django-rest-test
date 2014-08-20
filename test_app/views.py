from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cities.models import PostalCode
from .serializers import PostalCodeSerializer

@api_view(['GET'])
def get_state(request, params, format=None):
    params = params.split(',')
    if len(params) < 3:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    zipcode = params[2]

    try:
        postcode_data = PostalCode.objects.get(country__code='US', code=zipcode)
    except PostalCode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostalCodeSerializer(postcode_data)
        return Response(serializer.data)

