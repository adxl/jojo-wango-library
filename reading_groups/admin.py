from django.contrib import admin

from reading_groups.models import ReadingGroup,ReadingGroupHasUser

@admin.register(ReadingGroup)
class ReadingGroupAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ReadingGroup._meta.local_fields]

@admin.register(ReadingGroupHasUser)
class ReadingGroupAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ReadingGroupHasUser._meta.local_fields]
