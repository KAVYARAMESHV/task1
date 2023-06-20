from django.urls import path
from . import views

urlpatterns = [

    path('launch/', views.launching),


    path('product/', views.add_product),
    path('product_post/', views.product_post),
    path('view_product/', views.view_product),
    path('delete_product/<str:id>', views.delete_product),
    path('edit_product/<str:id>', views.edit_product),
    path('edit_post/', views.edit_post),


    path('login/',views.loginfun),
    path('login_post/',views.login_post),

    path('signup/',views.signup),
    path('signup_post/',views.signup_post),

    path('home/', views.home),
    path('userproduct/', views.userproduct),
    path('addcart/<str:id>', views.addtocart),
    path('cartpost/', views.cartpost),
    path('viewcart/', views.viewcart),
    path('deletcart/<str:id>', views.deletcart),

    path('ajax_add_qty/', views.ajax_add_qty),
    path('ajax_sub_qty/', views.ajax_sub_qty),
    path('viewcart_ajax/', views.viewcart_ajax),


]