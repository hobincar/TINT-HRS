from django.http import JsonResponse


def chat(request):
    data = {
        'message': request.GET.get('message', None)
    }
    return JsonResponse(data)