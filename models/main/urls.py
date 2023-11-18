from django.urls import path

from . import views

# 修改好以后需要在 主配置 python数据分析与可视化 目录下 的 urls.py 配置
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('movie/', views.movie, name='movie'),
    path('score/', views.score, name='score'),
    path('word/', views.word, name='word'),
    path('team/', views.team, name='team'),
]
