from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from app.models import Userprofile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
#import simplejson as json
#from django.utils import simplejson
try:
    import json
except ImportError:
    import simplejson as json

@csrf_exempt
def register(request):
    
    try:
        return_obj = {}
        attrs = json.loads(request.body)
        if 'username' in attrs:
            username = attrs['name']
            password = attrs['password']
            first_name = attrs['first_name']
            last_name = attrs['last_name']
            blood = attrs['blood']
            email = attrs['email']
            mobile = attrs['mobile']
            address = attrs['address']
            available = attrs['available']
            user_id = attrs['user_id']
            
            try:
                if attrs['gps_position'] != None and attrs['gps_position'] != "":
                    gps_loc = attrs['gps_position'].split(",")
                    lat = gps_loc[0]
                    long = gps_loc[1]
                else:
                    lat = 0
                    long = 0
            except:
                lat = 0
                long = 0
            
            if user_id != "" and user_id != None:
                user = Userprofile.objects.get(id=user_id)
                try:
                    user = Userprofile.objects.exclude(id = user_id).get(username=username)
                    return_obj['status'] = "fail"
                except:
                    user.username = name
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email
                    user.blood_group = blood
                    user.address = address
                    user.mobile_number = mobile
                    user.availability = available
                    user.latitude = lat
                    user.longitude = long
                    user.save()
                    return_obj['status'] = "success"
                    return_obj['id'] = user.id
                    return_obj['name'] = name
                    return_obj['blood'] = blood
                    return_obj['email'] = email
                    return_obj['mobile'] = mobile
                    return_obj['address'] = address
                    return_obj['available'] = available
            else:
                try:
                    user = Userprofile.objects.get(username=name)
                    return_obj['status'] = "fail"
                    return_obj['reason_for_fail'] = "Username exists, Please try another Username" 
                except:
                    user = Userprofile.objects.create(username=name,first_name=first_name,last_name=last_name,email=email,blood_group=blood,mobile_number=mobile,address=address,availability=available,latitude=lat,longitude=long)
                    user.set_password(password)
                    user.save()
                    return_obj['status'] = "success"
                    return_obj['id'] = user.id
                    return_obj['first_name'] = first_name
                    return_obj['last_name'] = last_name
                    return_obj['name'] = name
                    return_obj['password'] = password
                    return_obj['blood'] = blood
                    return_obj['email'] = email
                    return_obj['mobile'] = mobile
                    return_obj['address'] = address
                    return_obj['available'] = available
            
            return HttpResponse(json.dumps(return_obj))
    except Exception as e:    
        raise e

@csrf_exempt
def login(request):
    try:
        attrs = json.loads(request.body)
        name = attrs['username'].strip()
        password = attrs['password'].strip()
        
        return_obj = {}
        user = authenticate(username=name, password=password)
        if user:
            user = Userprofile.objects.get(id = user.id)
            return_obj['status'] = "success"
            return_obj['id'] = user.id
            return_obj['name'] = user.username
            return_obj['first_name'] = user.first_name
            return_obj['last_name'] = user.last_name
            return_obj['blood'] = user.blood_group
            return_obj['email'] = user.email
            return_obj['mobile'] = user.mobile_number
            return_obj['address'] = user.address
            return_obj['available'] = user.availability
        else:
            return_obj['status'] = "fail"
            return_obj['reason_for_fail'] = "Authentication Failure - Invalid username and password"
            
        return HttpResponse(json.dumps(return_obj))
    except Exception as e:    
        raise e

        

@csrf_exempt
def search(request):
    user_list = []
    latitude_deg = 1/111.12
    longitude_deg = 1/110.09
    try:
        return_obj = {}
        attrs = json.loads(request.body)
        if 'blood' in attrs:
            blood = attrs['blood']
            area = attrs['area']
            if attrs['gps_position'] != None and attrs['gps_position'] != "":
                gps_loc = attrs['gps_position'].split(",")
                lat = gps_loc[0]
                long = gps_loc[1]
            else:
                lat = 0
                long = 0
            if area == "all":
                users = Userprofile.objects.filter(blood_group = blood)
            else:
                lat_deg = latitude_deg * area
                pos_lat = lat_deg + deg
                neg_lat = lat_deg - deg
                
                long_deg = longitude_deg * area
                pos_long = long_deg + deg
                neg_long = long_deg - deg
                users = Userprofile.objects.filter(blood_group = blood,latitude__range =(pos_lat,neg_lat),longitude____range =(pos_long,neg_long))
                
                
            for user in users:
                obj = {}
                obj['name'] = user.username
                obj['mobile'] = user.mobile_number
                obj['address'] = user.address
                obj['email'] = user.email
                obj['available'] = user.availability
                user_list.append(obj)
                
            if user_list:
                return_obj['status'] = "success"
                return_obj['user_list'] = user_list
                return HttpResponse(json.dumps(return_obj))
            else:
                return_obj['status'] = "fail"
                return_obj['reason_for_fail'] = "No users found"
                return HttpResponse(json.dumps(return_obj))
    except Exception as e:    
        raise e


#change password
@csrf_exempt
def change_password(self, request):
    return_obj = {}
    
    try:
        
        attrs = json.loads(request.body)
        username = attrs["username"]
        old_password = attrs["old_password"]
        new_password = attrs["new_password"]
        
        user = authenticate(username=username, password=old_password)
        if user is not None and user.is_active:
            user.set_password(new_password)
            user.save()
            
            return_obj['password'] = new_password
            return_obj['status'] = "success"
        else:
            return_obj['status'] = "fail"
            return_obj['reason_for_failure'] = "Old password entered is invalid"                
        
        return json.dumps(return_obj)
    except Exception as e:    
        raise e