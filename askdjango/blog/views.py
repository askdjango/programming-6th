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

def hello_none(request):
    return HttpResponse('그냥 안녕!')

def hello(request, name, age=None):
    if age:
        message = '안녕하세요. {}님. {}세이시네요.'.format(name, age)
    else:
        message = '안녕하세요. {}님. 나이도 안 알려주고.'.format(name)

    # request.GET   # QueryDict : key 중복을 허용하는 dict
    # request.POST
    # request.FILES

    if 'name' in request.GET:
        name = request.GET['name']  # 값을 하나만 가져옴.
        name_list = ','.join(request.GET.getlist('name'))  # 다수 획득
        message += '''
        <ul>
            <li>{}</li>
            <li>{}</li>
        </ul>
        '''.format(name, name_list)

    return HttpResponse(message)


def mysum(request, arg):
    # arg  # "11321/12312/1231//123123/1231231///13123/"
    result = sum(int(i or 0) for i in arg.split('/'))
    return HttpResponse('결과는 {}입니다.'.format(result))

