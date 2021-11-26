from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from .tasks import send_report

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/home.html', data)



def send_email(request):
    send_report.delay()
    return HttpResponse('Task add in queue')