from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


api_patterns = [
    path('v1/', include('demo.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((api_patterns, 'api'))),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
