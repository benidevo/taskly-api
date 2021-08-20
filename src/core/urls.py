from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from users import router as users_api_router
from house import router as house_api_router
from task import router as task_api_router

auth_api_urls = [
    path('', include('rest_framework_social_oauth2.urls')),   
]

if settings.DEBUG:
    auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))

api_url_patterns = [
    path(r'auth/', include(auth_api_urls)),
    path(r'accounts/', include(users_api_router.router.urls)),
    path(r'house/', include(house_api_router.router.urls)),
    path(r'task/', include(task_api_router.router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
