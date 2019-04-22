#coding:utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from yml.forms import ProfileForm 
from yml.models import Profile
import urllib2
import json
import os
import argparse
import io

def index(request):
    return render(request, 'demo.html')

def list(request):
    context = {}
    form = ProfileForm
    context['form'] = form 
    pictures = Profile.objects.all()
    context['pictures'] = pictures
    show =False
    if Profile.objects.count():
        show=True
    print show
    return render(request, 'listing.html', context,show)

def item(request,a):
    c = int(a)
    print c
    name=["二校门","主楼","大礼堂","新清华学堂"]
    musicurl = "http://13.65.151.139:8000/static/music/"+a+".mp3"
    imgurl = "http://13.65.151.139:8000/static/img/"+a+".jpg"
    texturl = "http://13.65.151.139:8000/static/text/"+a+".txt"
    text = urllib2.urlopen(texturl).read()
    global zans
    zan = zans[c-1]
    return render(request, 'item.html', {'result': c,'spotname': name[c-1],'musicurl':musicurl,'imgurl':imgurl,'text':text,'zan':zan})

def save_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = Profile()
            profile.name = form.cleaned_data["picture"].name
            profile.picture = form.cleaned_data["picture"]
            profile.save()

        else:
            form = ProfileForm()

        return redirect(to='list')




