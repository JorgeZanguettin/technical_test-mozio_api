from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Providers, Polygons
from .serializers import ProvidersSerializer, PolygonsSerializer, PolygonsIncludesSerializer


@csrf_exempt
def polygons_list(request):
    """
        List all polygons, or create a new polygon.
    """
    if request.method == 'GET':
        polygons = Polygons.objects.all()
        serializer = PolygonsSerializer(polygons, many=True)
        return JsonResponse({'sucess': True, 'data': serializer.data}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            provider = Providers.objects.get(id=data['provider_id'])
            serializer_provider = ProvidersSerializer(provider)
            data['provider_name'] = serializer_provider.data['name']
        except Exception:
            return JsonResponse({'sucess': False, 'data': {'error': 'Provider Not Found'}}, status=400)

        serializer = PolygonsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'sucess': True, 'data': serializer.data}, status=201)
        return JsonResponse({'sucess': False, 'data': {'error': serializer.errors}}, status=400)
    else:
        return JsonResponse({'sucess': False, 'data': {'error': 'Method Not Allowed'}}, status=405)


@csrf_exempt
def polygons_detail(request, _id):
    """
        Retrieve, update or delete a polygon.
    """
    try:
        polygon = Polygons.objects.get(_id=_id)
    except Polygons.DoesNotExist:
        return JsonResponse({'sucess': False, 'data': {'error': 'polygon not exists'}}, status=400)

    if request.method == 'GET':
        serializer = PolygonsSerializer(polygon)
        return JsonResponse({'sucess': True, 'data': serializer.data})

    elif request.method == 'PUT':
        polygon = Polygons.objects.get(_id=_id)

        data = JSONParser().parse(request)
        serializer = PolygonsSerializer(polygon, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'sucess': True, 'data': serializer.data})
        return JsonResponse({'sucess': False, 'data': {'error': serializer.errors}}, status=400)

    elif request.method == 'DELETE':
        polygon.delete()
        return JsonResponse(data={'sucess': True, 'data': {}}, status=204)


@csrf_exempt
def providers_polygons_list(request, pk):
    """
        List all polygons of a provider
    """
    polygon = Polygons.objects.filter(provider_id=pk)

    if request.method == 'GET':
        serializer = PolygonsSerializer(polygon, many=True)

        return JsonResponse({'sucess': True, 'data': serializer.data})


@csrf_exempt
def providers_list(request):
    """
        List all providers, or create a new provider.
    """
    if request.method == 'GET':
        providers = Providers.objects.all()
        serializer = ProvidersSerializer(providers, many=True)
        return JsonResponse({'sucess': True, 'data': serializer.data}, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = ProvidersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'sucess': True, 'data': serializer.data}, status=201)
        return JsonResponse({'sucess': False, 'data': {'error': serializer.errors}}, status=400)
    else:
        return JsonResponse({'sucess': False, 'data': {'error': 'Method Not allowed'}}, status=405)


@csrf_exempt
def providers_detail(request, pk):
    """
        Retrieve, update or delete a provider.
    """
    try:
        provider = Providers.objects.get(pk=pk)
    except Providers.DoesNotExist:
        return JsonResponse({'sucess': False, 'data': {'error': 'provider not exists'}}, status=400)

    if request.method == 'GET':
        serializer = ProvidersSerializer(provider)
        return JsonResponse({'sucess': True, 'data': serializer.data})

    elif request.method == 'PUT':
        provider = Providers.objects.get(pk=pk)

        data = JSONParser().parse(request)
        serializer = ProvidersSerializer(provider, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'sucess': True, 'data': serializer.data})
        return JsonResponse({'sucess': False, 'data': {'error': serializer.errors}}, status=400)

    elif request.method == 'DELETE':
        provider.delete()
        return JsonResponse(data={'sucess': True, 'data': {}}, status=204)


@csrf_exempt
def polygons_list_by_coord(request, coord):
    """
        List all polygons of a coordinates
    """
    coords = list(map(lambda x: float(x), coord.split(',')))
    polygon = Polygons.objects.filter(geometry={
            "$geoIntersects": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": coords
                }
            }
        })

    if request.method == 'GET':
        serializer = PolygonsIncludesSerializer(polygon, many=True)

        return JsonResponse({'sucess': True, 'data': serializer.data})
