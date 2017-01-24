from django.http import HttpResponse
from django.shortcuts import render
import datetime


class NowTemplateView:
    @staticmethod
    def as_view(template_name=None):
        def view(request):
            now = datetime.datetime.now()
            if template_name is None:
                return HttpResponse('현재 시각은 {}입니다.'.format(now))
            return render(request, template_name, {
                'now': now,
            })
        return view


post_list = NowTemplateView.as_view('blog/post_list.html')

current_datetime = NowTemplateView.as_view()


def hello(request, name):
    return HttpResponse('안녕하세요. {}님.'.format(name))


def mysum(request, x, y, z=0):
    result = int(x) + int(y) + int(z)
    return HttpResponse('결과는 {}입니다.'.format(result))

