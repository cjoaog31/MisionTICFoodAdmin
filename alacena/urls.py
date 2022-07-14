from django.urls import path
from alacena import views

urlpatterns = [
    path('pantryCreation/', views.PantryCreateView.as_view()),

]