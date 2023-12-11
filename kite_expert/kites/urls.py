from django.urls import path
from django.views.decorators.cache import cache_page

from kites import views


urlpatterns = [
    path('', cache_page(60)(views.Index.as_view()), name='home'),
    path('brand/<slug:slug>/', cache_page(60)(views.Brand.as_view()), name='brand'),

    path('expert/<slug:slug>/', cache_page(60)(views.Expert.as_view()), name='expert'),
    path('expert/', cache_page(60)(views.Expert.as_view()), name='experts'),

    path('kite/add/', views.KiteAdd.as_view(), name='kiteadd'),
    path('kite/edit/<int:pk>/', views.KiteEdit.as_view(), name='kiteedit'),
    path('kite/del/<int:id>', views.kite_del, name='kitedel'),
    path('kite/<slug:slug>/', cache_page(60)(views.Kite.as_view()), name='kite'),

    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('profile/edit/<slug:slug>/', views.ExpertEdit.as_view(), name='expertedit'),
    path('profile/<slug:slug>/', views.UserProfile.as_view(), name='profile'),
]