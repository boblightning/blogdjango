from django.urls import path, include

from articles.views import article_list
from .views import article_form, article_list, article_details, register, update_article, user_login, delete_article
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', article_list, name = 'article_list'),
    path('articles/<slug:slug>/', article_details, name = 'article_details'),
    # path('login/', user_login, name = 'login'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', register, name = 'register'),
    path('password-change/', PasswordChangeView.as_view(), name = 'password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name = 'password_change_done'),
    path('add/', article_form, name = 'article_form'),
    path('update/<slug:slug>', update_article, name = 'update_article'),
    path('delete/<slug:slug>', delete_article, name = 'delete_article'),
]
