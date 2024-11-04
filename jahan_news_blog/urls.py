from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('accounts/login/', views.UserLoginView.as_view(), name='account_login'),
    path('accounts/signup/',views.UserSignupView.as_view(), name='account_signup'),
    path('accounts/profile/',views.UserProfileUpdateView.as_view(), name='profile'),
    path('news/write/',views.NewsArticleView.as_view(),name='createnews'),
    path('news/read/<int:pk>/',views.ReadArticleView.as_view(),name='readnews'),
    path('search/news/<str:category>/',views.Search.as_view(),name='search'),

]

