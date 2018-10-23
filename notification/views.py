from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .forms import UserForm
from .models import fcm_info, Users

from pyfcm import FCMNotification

def homePageView(request):
    prize = "<h1>Hello There</h1>"
    tokens = fcm_info.objects.all()
    for token in tokens:
        prize += token.fcm_token
    prize += '<br>'
    return HttpResponse(prize)

@csrf_exempt
def fcm_insert(request):
    token = request.GET.get("fcm_token", '')
    a = fcm_info(fcm_token=token)
    a.save()
    #print(a)
    return HttpResponse(token)


def send_notifications(request):
    path_to_fcm = "https://fcm.googleapis.com"
    server_key = 'AAAA89Z_XKc:APA91bG1PCvHqoX7yN65G8IA1EDirzMbwt74XqQaYplEJfoE8-WOxNShKUIYEXganwSN3E8hAry7FO6r8ws1X_heU99_0WaZ_ChM8R1UFa-auy0NT_WDHvgeLAcHUREmIT-uGJ8tQoJp'
    reg_id = fcm_info.objects.all()[0].fcm_token
    message_title = "Hi there"
    message_body = "vanshika"
    result = FCMNotification(api_key=server_key).notify_single_device(registration_id=reg_id, message_title=message_title, message_body=message_body)
    print(result)
    return HttpResponse(result)


@csrf_exempt
def add_user(request):
    phone=request.GET.get("phone_no",'')
    password=request.GET.get("password",'')
    new_user=Users(phone_no=phone,password=password)
    new_user.save()
    return HttpResponse(new_user)



@csrf_exempt
def check_credentials(request):
    if request.method =="POST":
        print("something"+str(request.body))
        s1=str(request.body)
        stri= s1.split("'")[1]
        print(stri)
        phone_no=stri.split('=')[1].split('&')[0]
        print(phone_no)
        password=stri.split('=')[2].split("'")[0]
        print(password)
        ob=get_object_or_404(Users,pk=phone_no).password
        print(ob)
        if ob==password:
            print('autheticate')
            return HttpResponse(status=201)
        else:
            print("don't authenticate")
            return HttpResponse(status=200)


