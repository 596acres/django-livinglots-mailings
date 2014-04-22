from django.contrib import admin

from .models import DeliveryRecord


class DeliveryRecordAdmin(admin.ModelAdmin):
    list_display = ('receiver_object', 'mailing', 'sent', 'recorded',)


admin.site.register(DeliveryRecord, DeliveryRecordAdmin)
