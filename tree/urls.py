from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addfact', views.addFact, name='afact'),
    path('editfact', views.editFact, name='efact'),
    path('deletefact', views.deleteFact, name='dfact'),
    path('deleteall', views.deleteAll, name='deleteall')
]
