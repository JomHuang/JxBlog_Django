"""
视图
"""

from django.http import HttpResponse,Http404,HttpResponseNotFound;
import datetime;


def index(request):
    return  HttpResponse("欢迎使用Django!");

def hello(request):
    return  HttpResponse("Hello ,");

def servertime(request):
    now = datetime.datetime.now()
    html = "<html><body>It's now %s.</body></html>" % now
    return HttpResponse(html)

#计算时间差
def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        #return HttpResponse("输入有误。 ")
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

