#project의 urls.py

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

