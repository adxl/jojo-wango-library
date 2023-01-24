from django.urls import include, path  # type: ignore

from reading_groups.views import add_reading_group, index, join_reading_group

urlpatterns = [
    path("reading-groups/", index, name="reading_groups"),
    path("reading-groups/add/", add_reading_group, name="reading_groups_add"),
    path("reading-groups/join/", join_reading_group, name="reading_groups_join"),
]
