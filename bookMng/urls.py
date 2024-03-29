from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('searchresults', views.searchresults, name='searchresults'),
    path('postcomment/<int:book_id>', views.postcomment, name='postcomment'),
    path('postrating/<int:book_id>', views.postrating, name='postrating'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('addtocart/<int:book_id>', views.addtocart, name='addtocart'),
    path('removefromcart/<int:book_id>', views.removefromcart, name='removefromcart')
]
