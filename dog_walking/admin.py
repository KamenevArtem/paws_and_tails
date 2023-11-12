
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase
from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = ('full_name', 'phone_number')
    list_display = ('full_name', 'phone_number')
    list_editable = ['phone_number']