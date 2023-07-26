import user_agents
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, re_path, path
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

SchemaView = get_schema_view(
    openapi.Info(
        title="Golibro API",
        default_version="v1",
        description="Imprimerie Gauvin application",
        terms_of_service="https://xxxxxxxxxxxx.com",
        contact=openapi.Contact(email="xxxxxx@golibro.ca"),
        license=openapi.License(name="Imprimerie Gauvin License ..."),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


def root_redirect(request):
    """
    redirect to documentation
    :param request:
    :return: redirect to home to documentation
    """
    user_agent_string = request.META.get("HTTP_USER_AGENT", "")
    user_agent = user_agents.parse(user_agent_string)
    schema_view = "cschema-swagger-ui"
    if user_agent.is_mobile:
        schema_view = "cschema-redoc"
    return redirect(schema_view, permanent=True)


# urlpatterns required for settings values
urlpatterns = i18n_patterns(
    re_path("swagger(?P<format>" + r"\.json|" + r"\.yaml)", SchemaView.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", SchemaView.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", SchemaView.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path("cached/swagger(?P<format>.json|.yaml)", SchemaView.without_ui(cache_timeout=None), name="cschema-json"),
    path("cached/swagger/", SchemaView.with_ui("swagger", cache_timeout=None), name="cschema-swagger-ui"),
    path("cached/redoc/", SchemaView.with_ui("redoc", cache_timeout=None), name="cschema-redoc"),
    path("docs/", include_docs_urls(title="golibro Api")),
    path("", root_redirect),
    path("api/", include("apps.users.urls")),
    path("api/", include("apps.common.urls")),
    path("accounts/", include("rest_framework.urls", namespace="rest_framework")),
    path(_("admin/"), admin.site.urls),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
