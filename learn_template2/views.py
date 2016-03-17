# -*- coding: utf-8 -*-  
from django.shortcuts import render

# Create your views here.

def home(request):
    input_str = '测试一下传入参数'
    return render(request, 'home2.html', {'content': input_str})