"""H1st IoT Data Management: models."""


import warnings

from django.db.models import (
    Model,
    CharField, DateField, FloatField, IntegerField,
    JSONField,
    ForeignKey, ManyToManyField,
    PROTECT)
from django.db.models.signals import m2m_changed, pre_delete

from h1st_iot.util import MAX_CHAR_LEN, clean_lower_str, clean_upper_str


# pylint: disable=line-too-long


class LogicalDataType(Model):
    """Logical Data Type."""

    name = \
        CharField(
            verbose_name='Logical Data Type',
            blank=False,
            null=False,
            unique=True,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    class Meta:
        """Metadata."""

        verbose_name = 'Logical Data Type'
        verbose_name_plural = 'Logical Data Types'

        ordering = ('name',)

    def __str__(self):
        """Return string repr."""
        return f'LogicalDataTp {self.name.upper()}'

    def save(self, *args, **kwargs):
        """Save."""
        self.name = clean_lower_str(self.name)
        super().save(*args, **kwargs)


class NumericMeasurementUnit(Model):
    """Numeric Measurement Unit."""

    name = \
        CharField(
            verbose_name='Numeric Measurement Unit',
            blank=False,
            null=False,
            unique=True,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    class Meta:
        """Metadata."""

        verbose_name = 'Numeric Measurement Unit'
        verbose_name_plural = 'Numeric Measurement Units'

        ordering = ('name',)

    def __str__(self):
        """Return string repr."""
        return f'NumMeasureUnit "{self.name}"'

    def save(self, *args, **kwargs):
        """Save."""
        self.name = self.name.strip()
        super().save(*args, **kwargs)


class EquipmentDataFieldType(Model):
    """Equipment Data Field Type."""

    name = \
        CharField(
            verbose_name='Equipment Data Field Type',
            blank=False,
            null=False,
            unique=True,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Data Field Type'
        verbose_name_plural = 'Equipment Data Field Types'

        ordering = ('name',)

    def __str__(self):
        """Return string repr."""
        return f'EqDataFldTp {self.name.upper()}'

    def save(self, *args, **kwargs):
        """Save."""
        self.name = clean_lower_str(self.name)
        super().save(*args, **kwargs)


class EquipmentGeneralType(Model):
    """Equipment General Type."""

    name = \
        CharField(
            verbose_name='Equipment General Type',
            blank=False,
            null=False,
            unique=True,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment General Type'
        verbose_name_plural = 'Equipment General Types'

        ordering = ('name',)

    def __str__(self):
        """Return string repr."""
        return f'EqGenTp {self.name.upper()}'

    def save(self, *args, **kwargs):
        """Save."""
        self.name = clean_lower_str(self.name)
        super().save(*args, **kwargs)


class EquipmentDataField(Model):
    """Equipment Data Field."""

    RELATED_NAME = 'equipment_data_fields'
    RELATED_QUERY_NAME = 'equipment_data_field'

    DEFAULT_UPPER_NUMERIC_NULL = 2 ** 30   # << MaxInt = 2 ** 31 - 1
    DEFAULT_LOWER_NUMERIC_NULL = -DEFAULT_UPPER_NUMERIC_NULL

    equipment_general_type = \
        ForeignKey(
            to=EquipmentGeneralType,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    name = \
        CharField(
            verbose_name='Equipment Data Field',
            blank=False,
            null=False,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    equipment_data_field_type = \
        ForeignKey(
            to=EquipmentDataFieldType,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    logical_data_type = \
        ForeignKey(
            to=LogicalDataType,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=True,
            null=True,
            on_delete=PROTECT)

    numeric_measurement_unit = \
        ForeignKey(
            to=NumericMeasurementUnit,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=True,
            null=True,
            on_delete=PROTECT)

    lower_numeric_null = \
        FloatField(
            blank=False,
            null=False,
            default=DEFAULT_LOWER_NUMERIC_NULL)

    upper_numeric_null = \
        FloatField(
            blank=False,
            null=False,
            default=DEFAULT_UPPER_NUMERIC_NULL)

    min_val = \
        FloatField(
            blank=True,
            null=True)

    max_val = \
        FloatField(
            blank=True,
            null=True)

    equipment_unique_types = \
        ManyToManyField(
            to='EquipmentUniqueType',
            related_name=RELATED_NAME + '_reverse',
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Data Field'
        verbose_name_plural = 'Equipment Data Fields'

        unique_together = 'equipment_general_type', 'name'

        ordering = 'equipment_general_type', 'name'

    def __str__(self):
        """Return string repr."""
        return ((f'{self.equipment_general_type.name.upper()} '
                 f'[{self.equipment_data_field_type.name}] '
                 f'{self.name} [') +
                (self.logical_data_type.name
                 if self.logical_data_type
                 else 'UNTYPED') +
                (f', unit {self.numeric_measurement_unit.name.upper()}'
                 if self.numeric_measurement_unit and self.numeric_measurement_unit.name   # noqa: E501
                 else '') +
                f', nulls ({self.lower_numeric_null}, {self.upper_numeric_null})' +   # noqa: E501
                (''
                 if self.min_val is None
                 else f', min {self.min_val}') +
                (''
                 if self.max_val is None
                 else f', max {self.max_val}') +
                ']')

    def save(self, *args, **kwargs):
        """Save."""
        self.name = clean_lower_str(self.name)
        super().save(*args, **kwargs)


class EquipmentUniqueTypeGroup(Model):
    """Equipment Unique Type Group."""

    RELATED_NAME = 'equipment_unique_type_groups'
    RELATED_QUERY_NAME = 'equipment_unique_type_group'

    equipment_general_type = \
        ForeignKey(
            to=EquipmentGeneralType,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    name = \
        CharField(
            verbose_name='Equipment Unique Type Group',
            blank=False,
            null=False,
            unique=True,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    equipment_unique_types = \
        ManyToManyField(
            to='EquipmentUniqueType',
            related_name=RELATED_NAME + '_reverse',
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    equipment_data_fields = \
        ManyToManyField(
            to=EquipmentDataField,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Unique Type Group'
        verbose_name_plural = 'Equipment Unique Type Groups'

        ordering = 'equipment_general_type', 'name'

    def __str__(self):
        """Return string repr."""
        return (f'{self.equipment_general_type.name.upper()} '
                f'UnqTpGrp {self.name.upper()}')

    def save(self, *args, **kwargs):
        """Save."""
        self.name = clean_lower_str(self.name)
        super().save(*args, **kwargs)


class EquipmentUniqueType(Model):
    """Equipment Unique Type."""

    RELATED_NAME = 'equipment_unique_types'
    RELATED_QUERY_NAME = 'equipment_unique_type'

    equipment_general_type = \
        ForeignKey(
            to=EquipmentGeneralType,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    name = \
        CharField(
            verbose_name='Equipment Unique Type',
            blank=False,
            null=False,
            unique=True,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    equipment_data_fields = \
        ManyToManyField(
            to=EquipmentDataField,
            through=EquipmentDataField.equipment_unique_types.through,
            related_name=RELATED_NAME + '_reverse',
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    equipment_unique_type_groups = \
        ManyToManyField(
            to=EquipmentUniqueTypeGroup,
            through=EquipmentUniqueTypeGroup.equipment_unique_types.through,
            related_name=RELATED_NAME + '_reverse',
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Unique Type'
        verbose_name_plural = 'Equipment Unique Types'

        ordering = 'equipment_general_type', 'name'

    def __str__(self):
        """Return string repr."""
        return (f'{self.equipment_general_type.name.upper()} '
                f'UnqTp {self.name.upper()}')

    def save(self, *args, **kwargs):
        """Save."""
        self.name = clean_lower_str(self.name)
        super().save(*args, **kwargs)


def equipment_unique_types_equipment_data_fields_m2m_changed(
        sender, instance, action, reverse, model, pk_set, using,
        *args, **kwargs):
    """M2M-changed signal."""
    # pylint: disable=too-many-arguments,too-many-branches,too-many-locals
    # pylint: disable=unused-argument

    if action == 'pre_add':
        invalid_objs = \
            model.objects \
            .filter(pk__in=pk_set) \
            .exclude(equipment_general_type=instance.equipment_general_type)

        if invalid_objs:
            warnings.warn(
                message=(f'*** {instance}: CANNOT ADD INVALID {invalid_objs} '
                         'WITH DIFFERENT EQUIPMENT GENERAL TYPE(S) ***'))

            pk_set.difference_update(
                i['pk']
                for i in invalid_objs.values('pk'))

    elif action in ('post_add', 'post_remove') and pk_set:
        if (model is EquipmentDataField) and \
                instance.equipment_unique_type_groups.count():
            equipment_unique_type_groups_to_update = \
                instance.equipment_unique_type_groups.all()

            print(
                f'{instance}: Changed Equipment Data Fields: {action.upper()}:'
                f' Updating Equipment Data Fields of {equipment_unique_type_groups_to_update}...'   # noqa: E501
            )

            for equipment_unique_type_group_to_update in \
                    equipment_unique_type_groups_to_update:
                equipment_unique_type_group_to_update.equipment_data_fields.set(   # noqa: E501
                    equipment_unique_type_group_to_update.equipment_unique_types.all()[0].equipment_data_fields.all().union(   # noqa: E501
                        *(equipment_unique_type.equipment_data_fields.all()
                          for equipment_unique_type in
                          equipment_unique_type_group_to_update.equipment_unique_types.all()[1:]),   # noqa: E501
                        all=False),
                    clear=False)

        elif model is EquipmentUniqueType:
            changed_equipment_unique_types = \
                model.objects.filter(pk__in=pk_set)

            equipment_unique_type_groups_to_update = \
                changed_equipment_unique_types[0].equipment_unique_type_groups.all().union(   # noqa: E501
                    *(equipment_unique_type.equipment_unique_type_groups.all()
                      for equipment_unique_type in changed_equipment_unique_types[1:]),   # noqa: E501
                    all=False)

            if equipment_unique_type_groups_to_update:
                print(
                    f'{instance}: Changed Equipment Unique Types: '
                    f'{action.upper()}: Updating Equipment Data Fields of '
                    f'{equipment_unique_type_groups_to_update} Related to '
                    f'Added/Removed {changed_equipment_unique_types}...')

                for equipment_unique_type_group_to_update in \
                        equipment_unique_type_groups_to_update:
                    equipment_unique_type_group_to_update.equipment_data_fields.set(   # noqa: E501
                        equipment_unique_type_group_to_update.equipment_unique_types.all()[0].equipment_data_fields.all().union(   # noqa: E501
                            *(equipment_unique_type.equipment_data_fields.all()
                              for equipment_unique_type in
                              equipment_unique_type_group_to_update.equipment_unique_types.all()[1:]),   # noqa: E501
                            all=False),
                        clear=False)

    elif action == 'pre_clear':
        if (model is EquipmentDataField) and \
                instance.equipment_unique_type_groups.count():
            equipment_unique_type_groups_to_update = \
                instance.equipment_unique_type_groups.all()

            print(
                f'*** {instance}: CLEARING Equipment Data Fields: '
                f'{action.upper()}: Updating Equipment Data Fields of '
                f'{equipment_unique_type_groups_to_update}... ***')

            for equipment_unique_type_group_to_update in \
                    equipment_unique_type_groups_to_update:
                remaining_equipment_unique_types = (
                    equipment_unique_type_group_to_update
                    .equipment_unique_types.exclude(pk=instance.pk))

                if remaining_equipment_unique_types.count():
                    equipment_unique_type_group_to_update.equipment_data_fields.set(   # noqa: E501
                        remaining_equipment_unique_types[0].equipment_data_fields.all().union(   # noqa: E501
                            *(remaining_equipment_unique_type.equipment_data_fields.all()   # noqa: E501
                              for remaining_equipment_unique_type in
                              remaining_equipment_unique_types[1:]),
                            all=False),
                        clear=False)

                else:
                    print(
                        f'*** {instance}: CLEARING Equipment Data Fields: '
                        f'{action.upper()}: CLEARING Equipment Data Fields '
                        f'of {equipment_unique_type_groups_to_update}... ***')

                    equipment_unique_type_group_to_update.equipment_data_fields.clear()   # noqa: E501

        elif (model is EquipmentUniqueType) and \
                instance.equipment_unique_types.count():
            equipment_unique_types_to_clear = \
                instance.equipment_unique_types.all()

            equipment_unique_type_groups_to_update = \
                equipment_unique_types_to_clear[0].equipment_unique_type_groups.all().union(   # noqa: E501
                    *(equipment_unique_type_to_clear.equipment_unique_type_groups.all()   # noqa: E501
                      for equipment_unique_type_to_clear in
                      equipment_unique_types_to_clear[1:]),
                    all=False)

            if equipment_unique_type_groups_to_update:
                print(
                    f'*** {instance}: CLEARING Equipment Unique Types: '
                    f'{action.upper()}: Updating Equipment Data Fields of '
                    f'{equipment_unique_type_groups_to_update} Related to '
                    f'{equipment_unique_types_to_clear} to Clear...')

                for equipment_unique_type_group_to_update in \
                        equipment_unique_type_groups_to_update:
                    first_equipment_unique_type = (
                        equipment_unique_type_group_to_update
                        .equipment_unique_types.all()[0])

                    equipment_unique_type_group_to_update.equipment_data_fields.set(   # noqa: E501
                        (first_equipment_unique_type.equipment_data_fields.exclude(pk=instance.pk)   # noqa: E501
                         if first_equipment_unique_type in equipment_unique_types_to_clear   # noqa: E501
                         else first_equipment_unique_type.equipment_data_fields.all()).union(   # noqa: E501
                            *((equipment_unique_type_group_equipment_unique_type.equipment_data_fields.exclude(pk=instance.pk)   # noqa: E501
                               if equipment_unique_type_group_equipment_unique_type in equipment_unique_types_to_clear   # noqa: E501
                               else equipment_unique_type_group_equipment_unique_type.equipment_data_fields.all())   # noqa: E501
                              for equipment_unique_type_group_equipment_unique_type in   # noqa: E501
                                equipment_unique_type_group_to_update.equipment_unique_types.all()[1:]),   # noqa: E501
                            all=False),
                        clear=False)


m2m_changed.connect(
    receiver=equipment_unique_types_equipment_data_fields_m2m_changed,
    sender=EquipmentUniqueType.equipment_data_fields.through,
    weak=True,
    dispatch_uid=None,
    apps=None)


def equipment_unique_type_groups_equipment_unique_types_m2m_changed(
        sender, instance, action, reverse, model, pk_set, using,
        *args, **kwargs):
    """M2M-changed signal."""
    # pylint: disable=too-many-arguments,too-many-branches,unused-argument

    if action == 'pre_add':
        invalid_objs = (
            model.objects
            .filter(pk__in=pk_set)
            .exclude(equipment_general_type=instance.equipment_general_type))

        if invalid_objs:
            warnings.warn(
                message=(f'*** {instance}: CANNOT ADD INVALID {invalid_objs} '
                         'WITH DIFFERENT EQUIPMENT GENERAL TYPE(S) ***'))

            pk_set.difference_update(
                i['pk']
                for i in invalid_objs.values('pk'))

    elif action in ('post_add', 'post_remove') and pk_set:
        if model is EquipmentUniqueType:
            if instance.equipment_unique_types.count():
                print(f'{instance}: Changed Equipment Unique Types: '
                      f'{action.upper()}: Updating Data Fields...')

                instance.equipment_data_fields.set(
                    instance.equipment_unique_types.all()[0].equipment_data_fields.all().union(   # noqa: E501
                        *(equipment_unique_type.equipment_data_fields.all()
                          for equipment_unique_type in
                          instance.equipment_unique_types.all()[1:]),
                        all=False),
                    clear=False)

            else:
                print(f'*** {instance}: REMOVED Equipment Unique Types: '
                      f'{action.upper()}: CLEARING Data Fields... ***')

                instance.equipment_data_fields.clear()

        elif model is EquipmentUniqueTypeGroup:
            equipment_unique_type_groups_to_update = \
                model.objects.filter(pk__in=pk_set)

            print(f'{instance}: Changed Equipment Unique Type Groups: '
                  f'{action.upper()}: Updating Data Fields of Added/Removed '
                  f'{equipment_unique_type_groups_to_update}...')

            for equipment_unique_type_group_to_update in \
                    equipment_unique_type_groups_to_update:
                if equipment_unique_type_group_to_update.equipment_unique_types.count():   # noqa: E501
                    equipment_unique_type_group_to_update.equipment_data_fields.set(   # noqa: E501
                        equipment_unique_type_group_to_update.equipment_unique_types.all()[0].equipment_data_fields.all().union(   # noqa: E501
                            *(equipment_unique_type.equipment_data_fields.all()
                              for equipment_unique_type in
                              equipment_unique_type_group_to_update.equipment_unique_types.all()[1:]),   # noqa: E501
                            all=False),
                        clear=False)

                else:
                    print(f'*** {equipment_unique_type_group_to_update}: '
                          f'REMOVED Equipment Unique Types: {action.upper()}: '
                          'CLEARING Data Fields... ***')

                    equipment_unique_type_group_to_update.equipment_data_fields.clear()   # noqa: E501

    elif action == 'pre_clear':
        if model is EquipmentUniqueType:
            print(f'*** {instance}: CLEARING Equipment Unique Types: '
                  f'{action.upper()}: CLEARING Data Fields... ***')

            instance.equipment_data_fields.clear()

        elif (model is EquipmentUniqueTypeGroup) and \
                instance.equipment_unique_type_groups.count():
            equipment_unique_type_groups_to_update = \
                instance.equipment_unique_type_groups.all()

            print(f'{instance}: CLEARING Equipment Unique Type Groups: '
                  f'{action.upper()}: Updating Data Fields of '
                  f'{equipment_unique_type_groups_to_update} to Clear...')

            for equipment_unique_type_group_to_update in \
                    equipment_unique_type_groups_to_update:
                remaining_equipment_unique_types = (
                    equipment_unique_type_group_to_update
                    .equipment_unique_types.exclude(pk=instance.pk))

                if remaining_equipment_unique_types.count():
                    equipment_unique_type_group_to_update.equipment_data_fields.set(   # noqa: E501
                        remaining_equipment_unique_types.all()[0].equipment_data_fields.all().union(   # noqa: E501
                            *(equipment_unique_type.equipment_data_fields.all()
                              for equipment_unique_type in
                              remaining_equipment_unique_types[1:]),
                            all=False),
                        clear=False)

                else:
                    print(f'*** {equipment_unique_type_group_to_update}: '
                          f'REMOVING Equipment Unique Types: {action.upper()}:'
                          f' CLEARING Data Fields... ***')

                    equipment_unique_type_group_to_update.equipment_data_fields.clear()   # noqa: E501


m2m_changed.connect(
    receiver=equipment_unique_type_groups_equipment_unique_types_m2m_changed,
    sender=EquipmentUniqueTypeGroup.equipment_unique_types.through,
    weak=True,
    dispatch_uid=None,
    apps=None)


def equipment_unique_type_pre_delete(sender, instance, using, *args, **kwargs):
    """Pre-Delete signal."""
    # pylint: disable=unused-argument

    if instance.equipment_unique_type_groups.count():
        equipment_unique_type_groups_to_update = \
            instance.equipment_unique_type_groups.all()

        print(f'*** DELETING {instance}: '
              'Updating Data Streams of '
              f'{equipment_unique_type_groups_to_update}... ***'   # noqa: E501
              )

        for equipment_unique_type_group_to_update in \
                equipment_unique_type_groups_to_update:
            remaining_equipment_unique_types = (
                equipment_unique_type_groups_to_update.equipment_unique_types
                .exclude(pk=instance.pk))

            if remaining_equipment_unique_types.count():
                equipment_unique_type_group_to_update.equipment_data_fields.set(   # noqa: E501
                    remaining_equipment_unique_types.all()[0].equipment_data_fields.all().union(   # noqa: E501
                        *(equipment_unique_type.equipment_data_fields.all()
                          for equipment_unique_type in
                          remaining_equipment_unique_types[1:]),
                        all=False),
                    clear=False)

            else:
                print(f'*** DELETING {instance}: '
                      f'CLEARING Data Streams of {equipment_unique_type_group_to_update}... ***'   # noqa: E501
                      )

                equipment_unique_type_group_to_update.equipment_data_fields.clear()   # noqa: E501


pre_delete.connect(
    receiver=equipment_unique_type_pre_delete,
    sender=EquipmentUniqueType,
    weak=True,
    dispatch_uid=None,
    apps=None)


class EquipmentFacility(Model):
    """Equipment Facility."""

    RELATED_NAME = 'equipment_facilities'
    RELATED_QUERY_NAME = 'equipment_facility'

    name = \
        CharField(
            verbose_name='Equipment Facility',
            blank=False,
            null=False,
            unique=True,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    info = \
        JSONField(
            blank=True,
            null=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Facility'
        verbose_name_plural = 'Equipment Facilities'

        ordering = ('name',)

    def __str__(self):
        """Return string repr."""
        return f'EqFacility "{self.name}"'

    def save(self, *args, **kwargs):
        """Save."""
        self.name = clean_lower_str(self.name)
        super().save(*args, **kwargs)


class EquipmentInstance(Model):
    """Equipment Instance."""

    RELATED_NAME = 'equipment_instances'
    RELATED_QUERY_NAME = 'equipment_instance'

    equipment_general_type = \
        ForeignKey(
            to=EquipmentGeneralType,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    equipment_unique_type = \
        ForeignKey(
            to=EquipmentUniqueType,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=True,
            null=True,
            on_delete=PROTECT)

    equipment_facility = \
        ForeignKey(
            to=EquipmentFacility,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=True,
            null=True,
            on_delete=PROTECT)

    name = \
        CharField(
            verbose_name='Equipment Instance',
            blank=False,
            null=False,
            unique=True,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    info = \
        JSONField(
            blank=True,
            null=True)

    equipment_unique_type_groups = \
        ManyToManyField(
            to=EquipmentUniqueTypeGroup,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Instance'
        verbose_name_plural = 'Equipment Instances'

        ordering = 'equipment_general_type', 'equipment_unique_type', 'name'

    def __str__(self):
        """Return string repr."""
        return (self.equipment_general_type.name.upper() +
                (f' UnqTp {self.equipment_unique_type.name}'
                 if self.equipment_unique_type
                 else '') +
                f' #{self.name}')

    def save(self, *args, **kwargs):
        """Save."""
        self.name = clean_lower_str(self.name)

        if self.equipment_unique_type and (
                self.equipment_unique_type.equipment_general_type !=
                self.equipment_general_type):
            warnings.warn(
                message=(f'*** EQUIPMENT INSTANCE #{self.name}: '
                         f'EQUIPMENT UNIQUE TYPE {self.equipment_unique_type} '
                         'NOT OF EQUIPMENT GENERAL TYPE '
                         f'{self.equipment_general_type} ***'))

            self.equipment_unique_type = None

        super().save(*args, **kwargs)


class EquipmentSystem(Model):
    """Equipment System."""

    RELATED_NAME = 'equipment_systems'
    RELATED_QUERY_NAME = 'equipment_system'

    equipment_facility = \
        ForeignKey(
            to=EquipmentFacility,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=True,
            null=True,
            on_delete=PROTECT)

    name = \
        CharField(
            verbose_name='Equipment System',
            blank=False,
            null=False,
            default=None,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    date = \
        DateField(
            blank=False,
            null=False,
            db_index=True)

    equipment_instances = \
        ManyToManyField(
            to=EquipmentInstance,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment System'
        verbose_name_plural = 'Equipment Systems'

        unique_together = 'name', 'date'

        ordering = 'equipment_facility', 'name', 'date'

    def __str__(self):
        """Return string repr."""
        return (self.name +
                (f' @ EqFacility "{self.equipment_facility.name}"'
                 if self.equipment_facility
                 else '') +
                f' on {self.date}')

    def save(self, *args, **kwargs):
        """Save."""
        self.name = clean_lower_str(self.name)
        super().save(*args, **kwargs)


class EquipmentUniqueTypeGroupDataFieldProfile(Model):
    """Equipment Unique Type Group Data Field Profile."""

    RELATED_NAME = 'equipment_unique_type_group_data_field_profiles'
    RELATED_QUERY_NAME = 'equipment_unique_type_group_data_field_profile'

    equipment_unique_type_group = \
        ForeignKey(
            to=EquipmentUniqueTypeGroup,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    equipment_data_field = \
        ForeignKey(
            to=EquipmentDataField,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    to_date = \
        DateField(
            blank=True,
            null=True,
            db_index=True)

    valid_proportion = \
        FloatField(
            blank=False,
            null=False)

    n_distinct_values = \
        IntegerField(
            blank=False,
            null=False)

    distinct_values = \
        JSONField(
            blank=True,
            null=True)

    sample_min = \
        FloatField(
            blank=True,
            null=True)

    outlier_rst_min = \
        FloatField(
            blank=True,
            null=True)

    sample_quartile = \
        FloatField(
            blank=True,
            null=True)

    sample_median = \
        FloatField(
            blank=True,
            null=True)

    sample_3rd_quartile = \
        FloatField(
            blank=True,
            null=True)

    outlier_rst_max = \
        FloatField(
            blank=True,
            null=True)

    sample_max = \
        FloatField(
            blank=True,
            null=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Unique Type Group Data Field Profile'
        verbose_name_plural = 'Equipment Unique Type Group Data Field Profiles'

        unique_together = \
            'equipment_unique_type_group', \
            'equipment_data_field', \
            'to_date'

        ordering = \
            'equipment_unique_type_group', \
            'equipment_data_field', \
            '-to_date'
