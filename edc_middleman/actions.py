

def reset_outgoing_transaction_middle_as_not_consumed(modeladmin, request, queryset):
    """ reset transaction by setting is_consumed_middleman = False"""
    for qs in queryset:
        qs.is_consumed_middleman = False
        qs.consumer = None
        qs.save()
reset_outgoing_transaction_middle_as_not_consumed.short_description = (
    "Set transactions as NOT consumed by MiddleMan(is_consumed_middleman=False)")
