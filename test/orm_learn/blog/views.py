from django.shortcuts import render
from orm_learn import settings
# Create your views here.


def index(request):
    # BASE_DIR = settings.STATICFILES_DIRS
    # print(BASE_DIR)
    return render(request,'blog/index.html')


def signin(request):
    return render(request,'blog/login.html')