from django.shortcuts import render
from django.views.generic import DetailView
from .models import Block


def index(request):
    block_list = Block.objects.all()
    return render(request, 'baseball/index.html', {
        'block_list': block_list,
    })


block_detail = DetailView.as_view(model=Block)

