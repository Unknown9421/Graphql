from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import *
from django.apps import apps
import json

# Create your views here.


def home(request):
    context = {}
    context['employees'] = Employee.objects.all()
    context['employees_json'] = json.dumps(list(Employee.objects.all().values('id', 'first_name', 'last_name', 'description', 'email',
                                             'country__name', 'rank', 'point')))



    return render(request, 'home.html', context)


def view_api(request, model_name):
    # models_db = {
    #     model._meta.model_name for model in apps.get_app_config('testgraphql').get_models()    # Quét tất cả models trong app (core)
    # }
    result_data = []
    data = {}
    data['status'] = True
    if request.method == 'GET':
        for query in apps.get_app_config('erp_system').get_model(model_name).objects.all():
            result_data.append(query.dictionary_parse)
        data['context'] = json.dumps(result_data)
        # print(data['context'])
    else:
        data['status'] = False
    return JsonResponse(data)