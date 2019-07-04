from . import views
from django.urls import path

urlpatterns = [
    path('',views.book),
    path('detail/<book_id>/<category_id>/',views.books_detail),
]