from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, weak=False, dispatch_uid="to_inspector_model_on_post_save")
def to_inspector_model_on_post_save(sender, instance, raw, created, using, **kwargs):
    if not raw:
        try:
            instance.to_inspector_model_on_post_save(instance, raw, created, using, **kwargs)
        except AttributeError as e:
            if 'to_inspector_model_on_post_save' not in str(e):
                raise AttributeError(str(e))
