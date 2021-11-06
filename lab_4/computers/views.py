from dataclasses import asdict

from django.shortcuts import render

from .models import Database


def master(request):
    names = Database.get_names()
    return render(request, 'index.html', {
        'data': {
            'names': names
        }
    })


def get_inf(request, name: str):
    mark = Database.get_mark_by_name(name)
    return render(
        request,
        'details.html',
        {
            'data': asdict(mark),
        },
    )
