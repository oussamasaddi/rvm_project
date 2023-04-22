from django.urls import path 
from . import views 
from . import machine 
from . import bottles 

urlpatterns = [
    path('',views.getAllusers),
    path('add/',views.addUser),
    path('getAllmachines/',machine.getAllmachines),
    path('addmachine/',machine.addMachine),
    path('<str:id>/deleteMachine/',machine.deleteMachine),
    path('<str:id>/updateMachine/',machine.updateMachine),
    path('searchM/', machine.searchMachines),
    path('deleteAllMachines/', machine.deleteAllMachines),
    path('addbottles/', bottles.addbottles),
    path('getAllbottles/', bottles.getAllbottles),
    path('<str:id>/deletebottle/',bottles.deletebottle),
    path('<str:id>/updateBottle/',bottles.updateBottle),
    path('search_B/',bottles.searchbottles),
    path('deleteAllbottles/', bottles.deleteAllMachines),







]
