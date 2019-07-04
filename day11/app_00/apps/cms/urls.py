from django.urls import path
from . import views
app_name = 'cms'
urlpatterns =[
    path('login/', views.SuperUserLoginView.as_view(), name='login'),
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('my_news/', views.my_news, name='my_news'),
    path('my_table/', views.mytable, name='my_table'),
    path('log_out/', views.logout, name='log_out'),
    path('user_info/', views.user_info, name='user_info'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('author_detail/', views.author_detail, name='author_detail'),
    path('add_article/', views.add_article, name='add_article'),
    path('add_author/', views.AddAuthorView.as_view(), name='add_author'),
    path('collection_del/', views.collection_del, name='collection_del'),
    path('collection_add/', views.collection_add, name='collection_add'),
]