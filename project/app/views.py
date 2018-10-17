from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import FormModel


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'app/index.html', context)


def userIndex(request):
    form_list = FormModel.objects.filter(username=request.user)
    context = {'form_list': form_list}
    return render(request, 'app/index.html', context)
