"""
URL configuration for python数据分析与可视化 project.

The `urlpatterns` list routes URLs to models. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function models
    1. Add an import:  from my_app import models
    2. Add a URL to urlpatterns:  path('', models.home, name='home')
Class-based models
    1. Add an import:  from other_app.models import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('models.main.urls')),
]
# 添加静态文件URL模式
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
