import user_agents
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, re_path
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.utils.translation import gettext_lazy as _
from rest_framework.documentation import include_docs_urls
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


schema_view = get_schema_view(
    openapi.Info(
        title="golibro API",
        default_version='v1',
        description="Imprimerie Gauvin application",
        terms_of_service="https://xxxxxxxxxxxx.com",
        contact=openapi.Contact(email="xxxxxx@golibro.ca"),
        license=openapi.License(name="Imprimerie Gauvin License ..."),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

def root_redirect(request):
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = user_agents.parse(user_agent_string)

    if user_agent.is_mobile:
        schema_view = 'cschema-redoc'
    else:
        schema_view = 'cschema-swagger-ui'

    return redirect(schema_view, permanent=True)

# urlpatterns required for settings values
required_urlpatterns = (
    path('admin/', admin.site.urls),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    re_path(r"^auth/", include("djoser.urls.jwt")),
)

urlpatterns = i18n_patterns(
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^cached/swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None), name='cschema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='cschema-swagger-ui'),
    path('cached/redoc/', schema_view.with_ui('redoc', cache_timeout=None), name='cschema-redoc'),

    path('', root_redirect),

    path('docs/', include_docs_urls(title='golibro Api')),
    path('', include("apps.users.urls")),

    path('accounts/', include('rest_framework.urls',
                              namespace='rest_framework')),

    path(_('admin/'), admin.site.urls),
    prefix_default_language=False,
) + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT, show_indexes=True)