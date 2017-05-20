from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from webchat import models


# Create your views here.


@login_required
def chat(request):
    return render(request,'webchat/chat.html')

@login_required
def send_msg(request):
    print(request.POST)
    return HttpResponse('------done-------')