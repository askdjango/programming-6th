from django.shortcuts import render
from .models import Webtoon


def webtoon_list(request):
    q = request.GET.get('q', '')
    qs = Webtoon.objects.all()

    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'webtoon/webtoon_list.html', {
        'webtoon_list': qs,
        'q': q,
    })


def webtoon_detail(request, id):
    webtoon = Webtoon.objects.get(id=id)  # DoesNotExist, MultipleObjectsReturned
    # webtoon = Webtoon.objects.filter(id=id)[0]  # IndexError
    return render(request, 'webtoon/webtoon_detail.html', {
        'webtoon': webtoon,
    })

