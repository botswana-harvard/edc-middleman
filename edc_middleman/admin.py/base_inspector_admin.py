from edc_base.modeladmin.admin import BaseModelAdmin


class BaseInspectorAdmin(BaseModelAdmin):

    list_display = ['item_identifier', 'app_name', 'model_name', 'is_consumed']

    list_filter = ['item_identifier', 'app_name', 'model_name', 'is_consumed']

    search_fields = ['item_identifier', 'app_name', 'model_name', 'is_consumed']
