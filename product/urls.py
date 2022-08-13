from django.urls import path
from product.views import productdetail, ProductListView, ProductDetailView,export,add_wishlist,my_wishlist,deleteFromWishlist,item


urlpatterns = [
    # path('productdetail/',productdetail,name="productdetail"),
    path('productlist/',ProductListView.as_view(),name="productlist"),
    path('productdetail/<int:pk>/',ProductDetailView.as_view(),name='productdetail'),
    path('export/', export, name='export'),
    path('add-wishlist',add_wishlist,name='add_wishlist'),
    path('my-wishlist',my_wishlist,name='my_wishlist'),
    path('delete-from-wishlist/',deleteFromWishlist,name="delete-from-wishlist"),
    path('delete/',item,name="delete"),
   
    # path('my-wishlist',my_wishlist,name='my_wishlist'),

]