from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.bookDetail, name='bookDetail'),
    path('buy/<int:book_id>/', views.buyBook, name='buyBook'),
    path('search/', views.search, name='search'),
]