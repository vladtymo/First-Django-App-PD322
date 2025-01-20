from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from test_project_pd import settings
from users.views import CustomLoginView

urlpatterns = [
    # path(r'^admin/login/', views.),
    path("", include("users.urls")),
    path("admin/", admin.site.urls),
    path("cart/", include("cart.urls")),
    path('login/', CustomLoginView.as_view(), name='login'),
]

if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
