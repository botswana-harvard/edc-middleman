from django.db import models


class InspectorCrfModelMixin(models.Model):
    """Mixin to create an inspector model for a CRF."""

    subject_identifier = models.CharField(
        max_length=25,
        verbose_name='Subject Identifier')

    requisition_datetime = models.DateTimeField(
        verbose_name='Requisition Date')

    requisition_identifier = models.CharField(
        max_length=50,
        verbose_name='Requisition Identifier')

    specimen_identifier = models.CharField(
        max_length=50,
        default='',
        null=True,
        blank=True,
        verbose_name='Specimen Identifier')

    device_id = models.CharField(
        max_length=15,
        verbose_name='Device Id')

    item_identifier = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        verbose_name='Item Identifier')

    app_name = models.CharField(
        max_length=25,
        verbose_name='Application Name')

    model_name = models.CharField(
        max_length=25,
        verbose_name='Model Name')

    is_confirmed = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name='Inspector confirmed')

    class Meta:
        abstract = True


class InspectorRequisitionModelMixin(InspectorCrfModelMixin):
    """Mixin to create an inspector model for a Requisition."""

    requisition_datetime = models.DateTimeField(
        verbose_name='Requisition Date')

    requisition_identifier = models.CharField(
        max_length=50,
        verbose_name='Requisition Identifier')

    specimen_identifier = models.CharField(
        max_length=50,
        default='',
        null=True,
        blank=True,
        verbose_name='Specimen Identifier')

    class Meta:
        abstract = True
