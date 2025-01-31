from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now

def api_info(request):
    data = {
        "email": "lewisnmutiso@gmail.com",
        "current_datetime": now().isoformat(),
        "github_url": "https://github.com/lewisnm/HNG-12_Internship.git"
    }
    return JsonResponse(data)

