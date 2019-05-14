from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from app.models import Userprofile
from django.contrib.auth.models import User
from django.utils import simplejson
#import simplejson as json


def webapp(request):
    return HttpResponseRedirect("/site_media/static/bgf/index.html")

def home(request):
    
    users = Userprofile.objects.all()
    
    return render_to_response("index.html",
                              {'users':users,},
                              context_instance = RequestContext(request),
                              )

@csrf_exempt
def home_info(request,id):
    print "gets here---------"
    returnobj = []
    obj = {}
    user = Userprofile.objects.get(id=id)
    obj['name'] = user.username
    obj['mobile'] = user.mobile_number
    obj['blood'] = user.blood_group
    returnobj.append(obj) 
    return HttpResponse(simplejson.dumps(returnobj), mimetype='application/javascript')
    