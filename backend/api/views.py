import json
from django.http import JsonResponse, request

# Create your views here.
def api_home(request, *args, **kwargs):
    body=request.body
    data={}
    try:
        data=json.loads(body)
    except:
        pass
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print('reached here')
    print(data.keys())
    print(request.headers)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return JsonResponse({"message":"Hi There! This is your Django API Home"})