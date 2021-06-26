from django.conf.urls import url
from core import views
from django.urls import path, include

urlpatterns = [
    url(r'^$', views.slide, name='otdel-slide'),
    path('all/', views.all, name='all'),
    path('<int:category_id>', views.cat_ord, name='cat_ord'),
    path('cards/<int:card_id>/', views.CardView.as_view(), name='card_detail'),
    path('all/search/', views.SearchResultsView.as_view(), name='search_results'),
]
