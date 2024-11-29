from django.urls import path
from . import views

app_name = 'sitesystem'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post-detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('strategy-list/', views.StrategyView.as_view(), name='strategy_list'),
    path('cheatcode-list/', views.CheatcodeView.as_view(), name='cheatcode_list'),
    path('rta-list/', views.RtaView.as_view(), name='rta_list'),
    path('news-list/', views.NewsView.as_view(), name='news_list'),
    path('comment/create/<int:pk>/', views.CommentView.as_view(), name='comment_form'),
]