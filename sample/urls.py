from django.contrib import admin
from django.urls import include, path

import kikeou.urls

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/",
        include(("django.contrib.auth.urls", "accounts"), namespace="accounts"),
    ),
    path("", include((kikeou.urls, "kikeou"), namespace="kikeou")),
]
