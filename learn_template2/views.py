# -*- coding: utf-8 -*-  
from django.shortcuts import render

# Create your views here.

def home(request):
    input_str = '测试一下传入参数'
    return render(request, 'home2.html', {'content': input_str})

def loop(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'loop.html', {'TutorialList': TutorialList})

def test_dict(request):
    info_dict = {'city': "Beijing", 'school': 'pku'}
    return render(request, 'dict.html', {'info_dict': info_dict})