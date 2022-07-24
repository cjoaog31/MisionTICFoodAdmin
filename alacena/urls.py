from django.urls import path
from alacena import views

urlpatterns = [
    path('pantryCreation/', views.PantryCreateView.as_view()),
    path('pantryList/', views.PantryListView.as_view()),
]