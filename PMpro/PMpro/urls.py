from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', login_required(TemplateView.as_view(template_name='index.html')), name="index"),
    url("", include('tasks.urls')),
    path("", include('users.urls'))
]

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

