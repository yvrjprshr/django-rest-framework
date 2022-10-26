from django.http import JsonResponse

# Create your views here.
def api_home(requests, *args, **kwargs):
    return JsonResponse({"message":"Hi There! This is your Django API Home"})