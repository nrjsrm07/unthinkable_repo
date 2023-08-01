# from .task import test_func
from .task import send_desktop_notifications
from django.http import HttpResponse


# Create your views here.
def test(request):
    # test_func.delay()
    send_desktop_notifications.delay()
    return HttpResponse("Done")
