from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def index_test(request):
    now=datetime.datetime.now()
    na="Django"
    fa="编程!"
    t=get_template('Index.html')
    html=t.render(Context({'nowdate':now,'name':na,'favourite':fa}))
    return HttpResponse(html)