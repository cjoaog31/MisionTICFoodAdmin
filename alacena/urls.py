from django.urls import path
from alacena import views

urlpatterns = [
    path('pantryCreation/', views.PantryCreateView.as_view()),
    path('pantryList/', views.PantryListView.as_view()),
    path('productAdd/', views.ProductAddView.as_view()),
    path('productEdit/', views.ProductEditView.as_view()),
    path('WishListAdd/', views.WishListAddProductView.as_view()),
    path('detailPantryProduct/', views.DetailPantryProductsView.as_view()),
    path('shoppingListCreate/', views.ShoppingListCreateView.as_view()),
]