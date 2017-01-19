from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return HttpResponse("안녕. 장고야. 넌 참 아름답구나.")
