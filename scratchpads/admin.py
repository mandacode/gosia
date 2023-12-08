from django.contrib import admin

from scratchpads.models import Scratchpad, ScratchpadRecord


@admin.register(Scratchpad)
class ScratchpadAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'created_at', 'updated_at')


@admin.register(ScratchpadRecord)
class ScratchpadRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'hours', 'date')
