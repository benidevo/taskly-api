from django.contrib import admin
from django.urls import path, include
from users import router as users_api_router

api_url_patterns = [
    path(r'accounts/', include(users_api_router.router.urls))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns))
]
