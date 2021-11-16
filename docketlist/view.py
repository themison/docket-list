from django.http.response import HttpResponse


def test(request):
    print('1')
    return HttpResponse(status=201)
