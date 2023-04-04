import json
import time
from urllib.parse import urlparse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

import redis

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

class VisitedDomainsView(APIView):
    def get(self, request, *args, **kwargs):
        p_from = request.GET.get('from')
        p_to = request.GET.get('to')
        if p_from == None or p_to == None\
                or not p_from.isdigit() or not p_to.isdigit():
            return Response({'status': 'invalid request parameters'}, status=status.HTTP_400_BAD_REQUEST)
        urls = set()
        for path_url in redis_instance.zrangebyscore('path_url_', int(p_from), int(p_to)):
            urls.add(json.loads(path_url)['url'])

        response = {
            'domains': urls,
            'status': 'ok'
        }
        return Response(response, status=status.HTTP_200_OK)

class VisitedLinksView(APIView):
    def post(self, request, *args, **kwargs):
        item = json.loads(request.body)
        key = list(item.keys())[0]
        value = item[key]
        if key == 'links':
            current_time = int(time.time())
            for url in value:
                parts = urlparse(url)
                path_url = parts.hostname if parts.hostname != None else parts.path
                unic_path = json.dumps({'time':current_time, 'url':path_url})
                redis_instance.zadd('path_url_', {unic_path: current_time})
            return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'json format unknown'}, status=status.HTTP_400_BAD_REQUEST)