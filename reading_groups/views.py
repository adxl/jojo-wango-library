from django.shortcuts import redirect, render
from django.template import loader
from django.utils import timezone

from reading_groups.forms import ReadingGroupForm
from reading_groups.models import ReadingGroup, ReadingGroupHasUser


def index(request):

    if request.user.profile.role == "LIBRARIAN":
        reading_groups_list: list[ReadingGroup] = ReadingGroup.objects.filter(
            end_at__gt=timezone.now()
        ).order_by("-start_at")
        context: dict[str, any] = {
            "reading_groups_list": reading_groups_list,
        }
        return render(request, "reading_groups/index.html", context)

    else:
        user_reading_groups = ReadingGroupHasUser.objects.all().filter(
            user=request.user.id
        )
        reading_groups_list: list[ReadingGroup] = ReadingGroup.objects.filter(
            end_at__gt=timezone.now()
        ).order_by("-start_at")
        context: dict[str, any] = {
            "reading_groups_list": reading_groups_list,
            "user_reading_groups": [g.group.id for g in user_reading_groups],
        }
        return render(request, "reading_groups/index.html", context)


def join_reading_group(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            group: ReadingGroup = ReadingGroup.objects.get(
                id=request.POST.get("group")
            )
            ReadingGroupHasUser.objects.create(user=request.user, group=group)

    return redirect("/reading-groups/")


def add_reading_group(request):
    if request.method == "POST":
        form = ReadingGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reading_groups")

    else:
        form = ReadingGroupForm()

    return render(
        request,
        "../templates/reading_groups/addReadingGroup.html",
        {"form": form},
    )


# Create your views here.
