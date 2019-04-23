#coding:utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from yml.forms import ProfileForm 
from yml.models import Profile
import urllib.request
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
    return render(request, 'listing.html', context)

def save_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = Profile()
            profile.name = form.cleaned_data["picture"].name
            profile.picture = form.cleaned_data["picture"]
            profile.save()
            mof="mv collected_static/uploads/test_pictures/"+profile.name+" yml/static/testimg/test.png"
            os.system(mof)
            ch="python ../super-resolution/super_resolve.py"
            os.system(ch)
            os.system("cp yml/static/testimg/test.png  ../EDSR-PyTorch/test/")
            os.chdir("../EDSR-PyTorch/src/")
            os.system("sh demo.sh")
            os.chdir("../../ist597final")
            os.system("mv ../EDSR-PyTorch/experiment/test/results-Demo/test_x4_SR.png yml/static/result/2.png")
        else:
            form = ProfileForm()
        return redirect(to='list')




