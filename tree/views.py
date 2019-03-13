from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Factory, Child
from .forms import AddFactoryForm, EditFactoryForm, DeleteFactoryForm

import random

def index(request):
    factory_list = Factory.objects.all()
    child_list = Child.objects.all()

    factory_name_list = []
    for f in factory_list:
        factory_name_list.append(f.name)

    afform = AddFactoryForm()
    efform = EditFactoryForm()
    dfform = DeleteFactoryForm()

    context = {'factory_list' : factory_list,
               'factory_name_list' : factory_name_list,
               'child_list'   : child_list,
               'afform'         : afform,
               'efform'         : efform,
               'dfform'         : dfform
              }
    
    return render(request, 'index.html', context)

@require_POST
def addFact(request):
    afform = AddFactoryForm(request.POST)
    
    if afform.is_valid():
        if int(request.POST['minimum']) <= int(request.POST['maximum']):
            new_factory = Factory(name=request.POST['name'], minimum=request.POST['minimum'], maximum=request.POST['maximum'])
            new_factory.save()
            random.seed()
            for i in range(int(request.POST['children'])):
                num = random.randint(int(request.POST['minimum']),int(request.POST['maximum']))
                new_child = Child(factory_id=Factory.objects.filter(name__exact=request.POST['name'])[0],value=num)
                new_child.save()

    return redirect('index')

@require_POST
def editFact(request):
    efform = EditFactoryForm(request.POST)

    factory_names = []
    for f in Factory.objects.all():
        factory_names.append(f.name)

    # I use this so I can break out if any of the values are invalid
    while True:
        # make sure the selected name is a current factory name
        if request.POST['select'] in factory_names:
            fact = Factory.objects.filter(name__exact=request.POST['select'])[0]

            # make sure name isn't already a factory name
            if request.POST['name'] in factory_names:
                break

            # make sure a new name was chosen
            if request.POST['name'] != 'none':
                fact.name = request.POST['name']

            # get the right mins and maxes
            if request.POST['minimum'] != 'none':
                temp_min = int(request.POST['minimum'])
            else:
                temp_min = fact.minimum

            if request.POST['maximum'] != 'none':
                temp_max = int(request.POST['maximum'])
            else:
                temp_max = fact.maximum

            # make sure the min and max are still logically sound
            if temp_min <= temp_max:
                fact.minimum = temp_min
                fact.maximum = temp_max

                # if there the max or min changing makes a child out of bounds, change to a new number in bounds
                for c in Child.objects.all():
                    if (c.factory_id.id == fact.id) and (c.value < temp_min or c.value > temp_max):
                        c.value = random.randint(temp_min, temp_max)
                        c.save()
            else:
                break

            fact.save()
        break


    return redirect('index')

@require_POST
def deleteFact(request):
    dfform = DeleteFactoryForm(request.POST)

    factory_names = []
    for f in Factory.objects.all():
        factory_names.append(f.name)

    if request.POST['select'] in factory_names:
            fact = Factory.objects.filter(name__exact=request.POST['select'])[0]
            for c in Child.objects.all():
                if c.factory_id == fact.id:
                    c.delete()
            fact.delete()

    return redirect('index')

def deleteAll(request):
    Child.objects.all().delete()
    Factory.objects.all().delete()

    return redirect('index')
