from django.contrib import admin
from .models import Transaction,Goal
# Register your models here.
# from import_export import resources
# from import_export.admin import ExportMixin
# class TransactionResource(resources.ModelResource):
#     class Meta:
#         model=Transaction
#         fields=('data','title','amount','transaction_type')

# class TransactionAdmin(ExportMixin,admin.ModelAdmin):
#     resource_class=TransactionResource
#     list_display=('date','title','amount','transaction_type')
#     search_fields=('title',)

admin.site.register(Transaction)
admin.site.register(Goal)

