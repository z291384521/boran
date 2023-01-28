"""boran URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
# from app01.views import admin
# from login import view
from app01.views import depart
from app01.views import game
from app01.views import user
# 访问inex/ 执行views.index
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('index/', views.index),
    # path('user_list/', views.user_list),
    # path('user_add/', views.user_add),
    # path('template/', views.template),
    # path('request/', views.something),
    # # 用户登录测试
    # path('logintest/', views.logintest),
    # # 测试ORM
    # path("orm/", views.ORM),
    # # 小案例info_list
    # path("info_list/", views.info_list),
    # path("info_add/", views.info_add),
    # path("info_delete/", views.info_delete),
    # 小案例
    path("depart/list/", depart.depart_list),
    path("depart/add/", depart.depart_add),
    path("depart/delete/", depart.depart_delete),
    # 正则匹配如下表达式
    # http://127.0.0.1:8000/depart/10/edit
    path("depart/<int:nid>/edit/", depart.depart_edit),

    # path("depart/", depart.index),
    path("user/list/", user.user_list),
    path("user/add/", user.user_add),
    path("user/model/form/add/", user.user_model_form_add),
    path("user/<int:nid>/edit/", user.user_edit),

    # #管理员管理
    # path("admin/list/", admin.user_list),
    #号列表
    path("game/list/", game.game_list),
    path("game/add/", game.game_add),
    path("game/<int:nid>/edit/", game.game_edit),
]

