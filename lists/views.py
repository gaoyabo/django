# coding:utf-8
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(u"欢迎来到自强学堂！")    
