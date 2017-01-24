from django.http import HttpResponse
from django.shortcuts import render
import datetime


def post_list(request):
    '''
    request.user
    request.META['HTTP_USER_AGENT']
    request.META['REMOTE_ADDR']
    request.GET
    request.POST
    request.FILES
    request.session
    '''

    now = datetime.datetime.now()

    return render(request, 'blog/post_list.html', {
        'now': now,
    })


def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse('현재 시간은 <b>{}</b> 입니다.'.format(now))
