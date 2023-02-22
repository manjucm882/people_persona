from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path('',views.apiOverview,name='apiOverview')

    path('people-list/',views.ShowAll,name='people-list'),
    path('people-detail/<int:pk>/',views.ViewPeople,name='people-detail'),
    path('people-add/',views.AddPeople,name='people-add'),
    path('people-update/<int:pk>/',views.UpdatePeople,name='people-update'),
    path('people-delete/<int:pk>/',views.DeletePeople,name='people-delete')
] 