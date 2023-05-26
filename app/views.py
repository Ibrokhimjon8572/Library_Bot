import requests
import json

from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

BOT_TOKEN = getattr(settings, "BOT_TOKEN")
ACCESS_TOKEN = getattr(settings, "ACCESS_TOKEN")


def authorize(request):
    return 'Authorization' in request.headers \
        and request.headers['Authorization'] == ACCESS_TOKEN

@csrf_exempt
def set_webhook(request):
    if request.method != "POST":
        return JsonResponse(status=400, data={
            'status': False,
            'message': 'Only post method is allowed',
        })

    body = json.loads(request.body)
    r = requests.get('https://api.telegram.org/bot' + BOT_TOKEN +
            '/setwebhook?url=https://' + body['url'] + '/bot/')
    res = r.json()
    
    return JsonResponse(status=200, data={
        'status': True,
        'message': res
    })

