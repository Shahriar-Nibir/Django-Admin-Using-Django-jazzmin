from system.models import SessionDetail
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import math
import random
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.gis.geoip2 import GeoIP2
from datetime import datetime
from cms.models import Page
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


otp_key = {}
id_user = {}


def home(request):
    return render(request, 'home.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def password(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            session = request.session
            session_key = session.session_key
            if session_key == None:
                logout(request)
                messages.info(request, "Incorrect Credentials")
                return redirect('password')
            print(session_key)
            login_time = datetime.now()
            # print(request.session['key'])
            user_agent = request.META['HTTP_USER_AGENT']
            device_family = request.user_agent.device.family
            browser = request.user_agent.browser.family
            os = request.user_agent.os.family
            browser_version = request.user_agent.browser.version_string
            os_version = request.user_agent.browser.version_string
            remote_ip = get_client_ip(request)
            is_active = True
            g = GeoIP2()
            try:
                remote_ip_country = g.city(remote_ip)['country_code']
                print(remote_ip_country)
            except:
                remote_ip_country = 'AE'
            session = SessionDetail.objects.create(user=user, token=session_key, remote_ip=remote_ip, user_agent=user_agent, device_family=device_family,
                                                   remote_ip_country=remote_ip_country, browser=browser, os=os, os_version=os_version, login_time=login_time, is_active=is_active)
            session.save()
            return redirect('test')
            # else:
            #    return redirect('user')
        else:
            messages.info(request, "Incorrect Credentials")
    return render(request, 'password.html')


def logoutUser(request):
    logout_time = datetime.now()
    session = request.session
    session_key = session.session_key

    try:
        sd = SessionDetail.objects.get(token=session_key)
    except:
        user_agent = request.META['HTTP_USER_AGENT']
        sd = SessionDetail.objects.get(user_agent=user_agent)
        print(session_key)
    sd.logout_time = logout_time
    sd.is_active = False
    sd.save()
    logout(request)
    logout_time = datetime.now()
    return redirect('home')


def otp(request):
    print('hello')
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.get(username=username)
        email = user.email
        print(email)
        o = generateOTP()
        htmlgen = '<p>Your OTP is <strong>o</strong></p>'
        send_mail('OTP request', o, '<your gmail id>', [
                  email], fail_silently=False, html_message=htmlgen)
        print(o)
        otp = o[0]
        id = o[1]
        otp_key[id] = otp
        id_user[id] = user
        return redirect('checkOtp', pk=id)
    return render(request, 'otp.html')


def checkOtp(request, pk):
    id = pk
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp == otp_key[id]:
            user = id_user[id]
            if user is not None:
                login(request, user)
                session = request.session
                session_key = session.session_key
                print(session_key)
                login_time = datetime.now()
                # print(request.session['key'])
                user_agent = request.META['HTTP_USER_AGENT']
                device_family = request.user_agent.device.family
                browser = request.user_agent.browser.family
                os = request.user_agent.os.family
                browser_version = request.user_agent.browser.version_string
                os_version = request.user_agent.browser.version_string
                remote_ip = get_client_ip(request)
                is_active = True
                g = GeoIP2()
                try:
                    remote_ip_country = g.city(remote_ip)['country_code']
                    print(remote_ip_country)
                except:
                    remote_ip_country = 'AE'
                session = SessionDetail.objects.create(user=user, token=session_key, remote_ip=remote_ip, user_agent=user_agent, device_family=device_family,
                                                       remote_ip_country=remote_ip_country, browser=browser, os=os, os_version=os_version, login_time=login_time, is_active=is_active)
                session.save()
                return redirect('test')
            else:
                messages.info(request, "Incorrect Credentials")
        else:
            messages.info(request, "Wrong OTP")
    return render(request, 'checkOtp.html')


@login_required(login_url='home')
def logoutEach(request, pk):
    sd = SessionDetail.objects.get(id=pk)
    time = datetime.now()
    sd.logout_time = time
    sd.is_active = False
    sd.save()
    try:
        s = Session.objects.get(session_key=sd.token)
        s.delete()
    except:
        pass
    return redirect('http://127.0.0.1:8000/admin/system/sessiondetail/')


@login_required(login_url='home')
def test(request):
    u = request.user
    user = AppUser.objects.get(user=u)
    groups = user.groups
    page_all = []
    for g in groups.all():
        print(g)
        pages = Page.objects.filter(groups=g)
        page_all.append(pages)
    print(page_all)
    context = {'page': page_all}
    return render(request, 'dashboard.html', context)


def generateOTP():
    digits = "0123456789"
    OTP = ""
    id = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
        id += digits[math.floor(random.random() * 10)]
    return OTP, id


@login_required(login_url='home')
def profile(request):
    u = request.user
    user = AppUser.objects.get(user=u)
    context = {'user': user}
    return render(request, 'profile.html', context)
