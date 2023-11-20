from django.contrib import admin
from django.urls import path
from . import views
app_name="myapp"
urlpatterns = [
    path('splash/',views.index,name="splash"),
    path('products/' , views.listProduct,name="products"),
    path('product/<int:id>/',views.detailProduct,name="productDetail"),
    path("product/addProduct/", views.addProduct, name="addProduct"),
    path("product/updateProduct/<int:id>/", views.updateProduct, name="updateProduct"),
    path("product/deleteProduct/<int:id>/", views.deleteProduct, name="deleteProduct"),

]
