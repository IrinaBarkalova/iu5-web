from dataclasses import asdict

from django.shortcuts import render

from computers.models import PCMark, PCModel


def master(request):
    name = PCMark.objects.all()
    return render(request, 'index.html', {'data': {
        'name': name
    }})


def get_inf(request, name: str):
    post = PCModel.objects.select_related("pc_mark").filter(pc_mark__name=name).all()
    return render(
        request,
        'details.html',
        {
            'data': post,
        },
    )
