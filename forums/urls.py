from django.urls import include, path  # type: ignore

from forums.views import index

urlpatterns = [
    path('forum/forum_channel/<str:id>', index, name="forum_channel"),
]
