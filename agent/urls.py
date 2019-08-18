from django.urls import path

from .views import update_profile, agent_plant_create

urlpatterns = [
    path('', update_profile, name='create'),
    path('<int:agent_pk>/plants/', agent_plant_create, name='plant_create')
]