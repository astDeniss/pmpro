from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from users.views import signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name='index.html'), name="index"),
    url("", include('tasks.urls')),
    path('signup/', signup_view, name="signup")
]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

