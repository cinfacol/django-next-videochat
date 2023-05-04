from django.contrib import admin
from django.urls import include, path

from videochat.views import chatPage, index

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("", index, name="home"),
    path("chat/<str:username>/", chatPage, name="chat"),
]
