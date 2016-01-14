from datetime import datetime

from django.db import models

from edc_device import device


class MiddlemanModelMixin(models.Model):

    """Add to a model class for the concrete model to update/create an inspector model."""

    inspector_model = None

    def to_inspector_model(self, fields, instance_pk, using):
        """Creates or updates an inspector model instance for the concrete model."""
        subject_identifier = fields.get('subject_identifier')
        requisition_datetime = datetime.strptime(str(fields.get('requisition_datetime')), '%Y-%m-%dT%H:%M:%S'),
        requisition_identifier = fields.get('requisition_identifier', instance_pk)
        specimen_identifier = fields.get('specimen_identifier', instance_pk)
        try:
            inspector_model = self.inspector_model.objects.using(using).get(
                subject_identifier=subject_identifier,
                requisition_identifier=requisition_identifier)
            inspector_model.requisition_datetime = requisition_datetime
            inspector_model.device_id = str(device)
            inspector_model.app_name = self._meta.app_label
            inspector_model.model_name = self._meta.object_name
            inspector_model.save()
        except self.inspector_model.DoesNotExist:
            self.inspector_model.objects.using(using).create(
                requisition_datetime=requisition_datetime,
                subject_identifier=subject_identifier,
                requisition_identifier=requisition_identifier,
                specimen_identifier=specimen_identifier,
                device_id=str(device),
                app_name=self._meta.app_label,
                model_name=self._meta.object_name)

    class Meta:
        abstract = True
