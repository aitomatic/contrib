"""H1st IoT Maintenance Operations: models."""


from datetime import timedelta

from django.db.models import (
    Model,
    BigAutoField, BooleanField, CharField, DateField, DateTimeField,
    FloatField, PositiveSmallIntegerField, IntegerField, TextField,
    JSONField,
    ForeignKey, ManyToManyField,
    PROTECT)
from django.db.models.constraints import UniqueConstraint
from django.db.models.signals import post_save
from django.contrib.postgres.fields import DateRangeField

from psycopg2.extras import DateRange

from aito.iot_mgmt.data.models import (EquipmentUniqueTypeGroup,
                                       EquipmentInstance)
from aito.iot_mgmt.utils import MAX_CHAR_LEN, clean_lower_str


_ONE_DAY_TIME_DELTA = timedelta(days=1)
_ONE_DAY_TIME_DELTA_TOTAL_SECONDS = _ONE_DAY_TIME_DELTA.total_seconds()


# pylint: disable=line-too-long


class EquipmentInstanceDailyRiskScore(Model):
    """Equipment Instance Daily Risk Score."""

    RELATED_NAME = 'equipment_instance_daily_risk_scores'
    RELATED_QUERY_NAME = 'equipment_instance_daily_risk_score'

    id = BigAutoField(
        primary_key=True)

    equipment_unique_type_group = \
        ForeignKey(
            to=EquipmentUniqueTypeGroup,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    equipment_instance = \
        ForeignKey(
            to=EquipmentInstance,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    risk_score_name = \
        CharField(
            blank=False,
            null=False,
            db_index=True,
            max_length=MAX_CHAR_LEN)

    date = \
        DateField(
            blank=False,
            null=False,
            db_index=True)

    risk_score_value = \
        FloatField(
            blank=False,
            null=False)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Instance Daily Risk Score'
        verbose_name_plural = 'Equipment Instance Daily Risk Scores'

        unique_together = \
            'equipment_unique_type_group', \
            'equipment_instance', \
            'risk_score_name', \
            'date'

    def __str__(self):
        """Return string repr."""
        return (f'{self.equipment_unique_type_group.equipment_general_type.name} '  # noqa: E501
                f'{self.equipment_unique_type_group.name} '
                f'#{self.equipment_instance.name} on {self.date}: '
                f'{self.risk_score_name} = {self.risk_score_value:.3g}')


class EquipmentProblemType(Model):
    """Equipment Problem Type."""

    name = \
        CharField(
            verbose_name='Equipment Problem Type',
            max_length=MAX_CHAR_LEN,
            blank=False,
            null=False,
            unique=True,
            db_index=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Problem Type'
        verbose_name_plural = 'Equipment Problem Types'

        ordering = ('name',)

    def __str__(self):
        """Return string repr."""
        return f'EqProbTp "{self.name}""'

    def save(self, *args, **kwargs):
        """Save."""
        self.name = self.name.strip()
        super().save(*args, **kwargs)


class EquipmentInstanceDailyPredictedFault(Model):
    """Equipment Instance Daily Predicted Fault."""

    RELATED_NAME = 'equipment_instance_daily_predicted_faults'
    RELATED_QUERY_NAME = 'equipment_instance_daily_predicted_fault'

    id = BigAutoField(
        primary_key=True)

    equipment_unique_type_group = \
        ForeignKey(
            verbose_name='Equipment Unique Type Group',
            help_text='Equipment Unique Type Group',
            to=EquipmentUniqueTypeGroup,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    equipment_instance = \
        ForeignKey(
            verbose_name='Equipment Instance',
            help_text='Equipment Instance',
            to=EquipmentInstance,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    date = \
        DateField(
            verbose_name='Date',
            help_text='Date',
            blank=False,
            null=False,
            db_index=True)

    fault_type = \
        ForeignKey(
            verbose_name='Fault Type',
            help_text='Fault Type',
            to=EquipmentProblemType,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    fault_predictor_name = \
        CharField(
            verbose_name='Fault Predictor Name',
            help_text='Fault Predictor Name',
            max_length=MAX_CHAR_LEN,
            blank=False,
            null=False,
            db_index=True)

    predicted_fault_probability = \
        FloatField(
            verbose_name='Predicted Fault Probability',
            help_text='Predicted Fault Probability',
            blank=False,
            null=False)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Instance Daily Predicted Fault'
        verbose_name_plural = 'Equipment Instance Daily Predicted Faults'

        constraints = (
            UniqueConstraint(
                fields=('equipment_unique_type_group',
                        'equipment_instance',
                        'date',
                        'fault_type',
                        'fault_predictor_name'),
                name='EquipmentInstanceDailyPredictedFault_unique_together'),
        )

    def __str__(self):
        """Return string repr."""
        return (f'{self.equipment_unique_type_group.equipment_general_type.name} '  # noqa: E501
                f'{self.equipment_unique_type_group.name} '
                f'#{self.equipment_instance.name} on {self.date}: '
                f'{self.fault_type.name.upper()} predicted '
                f'w/ prob {100 * self.predicted_fault_probability:.1f}% '
                f'by {self.fault_predictor_name}')


class EquipmentInstanceAlarmPeriod(Model):
    """Equipment Instance Alarm Period."""

    RELATED_NAME = 'equipment_instance_alarm_periods'
    RELATED_QUERY_NAME = 'equipment_instance_alarm_period'

    equipment_instance = \
        ForeignKey(
            to=EquipmentInstance,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    alarm_type = \
        ForeignKey(
            to=EquipmentProblemType,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    from_utc_date_time = \
        DateTimeField(
            blank=False,
            null=False,
            db_index=True)

    to_utc_date_time = \
        DateTimeField(
            blank=True,
            null=True,
            db_index=True)

    duration_in_days = \
        FloatField(
            blank=True,
            null=True,
            db_index=True)

    date_range = \
        DateRangeField(
            blank=True,
            null=True)

    equipment_instance_alert_periods = \
        ManyToManyField(
            to='EquipmentInstanceAlertPeriod',
            related_name=RELATED_NAME + '_reverse',
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    has_associated_equipment_instance_alert_periods = \
        BooleanField(
            blank=False,
            null=False,
            default=False,
            db_index=True)

    equipment_instance_problem_diagnoses = \
        ManyToManyField(
            to='EquipmentInstanceProblemDiagnosis',
            related_name=RELATED_NAME + '_reverse',
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    has_associated_equipment_instance_problem_diagnoses = \
        BooleanField(
            blank=False,
            null=False,
            default=False,
            db_index=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Instance Alarm Period'
        verbose_name_plural = 'Equipment Instance Alarm Periods'

        unique_together = \
            'equipment_instance', \
            'alarm_type', \
            'from_utc_date_time'

        ordering = 'equipment_instance', '-from_utc_date_time'

    def __str__(self):
        """Return string repr."""
        return ((f'{self.equipment_instance}: {self.alarm_type.name.upper()} '
                 f'from {self.from_utc_date_time}') +  # noqa: W504
                (f' to {self.to_utc_date_time} ({self.duration_in_days:.3f} Days)'  # noqa: E501
                 if self.to_utc_date_time
                 else ' (ONGOING)'))

    def save(self, *args, **kwargs):
        """Save."""
        if self.to_utc_date_time:
            self.duration_in_days = (
                (self.to_utc_date_time -  # noqa: W504
                 self.from_utc_date_time).total_seconds()
            ) / _ONE_DAY_TIME_DELTA_TOTAL_SECONDS

            _to_date = (self.to_utc_date_time + _ONE_DAY_TIME_DELTA).date()

        else:
            self.duration_in_days = _to_date = None

        self.date_range = \
            DateRange(
                lower=(self.from_utc_date_time - _ONE_DAY_TIME_DELTA).date(),
                upper=_to_date,
                bounds='[]',
                empty=False)

        super().save(*args, **kwargs)


class EquipmentInstanceProblemDiagnosis(Model):
    """Equipment Instance Problem Diagnosis."""

    RELATED_NAME = 'equipment_instance_problem_diagnoses'
    RELATED_QUERY_NAME = 'equipment_instance_problem_diagnosis'

    equipment_instance = \
        ForeignKey(
            to=EquipmentInstance,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    from_date = \
        DateField(
            blank=False,
            null=False,
            db_index=True)

    to_date = \
        DateField(
            blank=True,
            null=True,
            db_index=True)

    date_range = \
        DateRangeField(
            blank=True,
            null=True)

    duration = \
        IntegerField(
            blank=True,
            null=True)

    equipment_problem_types = \
        ManyToManyField(
            to=EquipmentProblemType,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    has_equipment_problems = \
        BooleanField(
            blank=False,
            null=False,
            default=False,
            db_index=True)

    dismissed = \
        BooleanField(
            blank=False,
            null=False,
            default=False,
            db_index=True)

    comments = \
        TextField(
            blank=True,
            null=True)

    equipment_instance_alarm_periods = \
        ManyToManyField(
            to=EquipmentInstanceAlarmPeriod,
            through=(EquipmentInstanceAlarmPeriod
                     .equipment_instance_problem_diagnoses.through),
            related_name=RELATED_NAME + '_reverse',
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    has_associated_equipment_instance_alarm_periods = \
        BooleanField(
            blank=False,
            null=False,
            default=False,
            db_index=True)

    equipment_instance_alert_periods = \
        ManyToManyField(
            to='EquipmentInstanceAlertPeriod',
            related_name=RELATED_NAME + '_reverse',
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    has_associated_equipment_instance_alert_periods = \
        BooleanField(
            blank=False,
            null=False,
            default=False,
            db_index=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Instance Problem Diagnosis'
        verbose_name_plural = 'Equipment Instance Problem Diagnoses'

        unique_together = 'equipment_instance', 'from_date'

        ordering = 'dismissed', '-to_date', 'from_date'

    def __str__(self):
        """Return string repr."""
        return (f'{self.equipment_instance} from {self.from_date} ' +
                (f'to {self.to_date}'
                 if self.to_date
                 else '(ONGOING)') +
                (': {}'.format(   # pylint: disable=consider-using-f-string
                    ', '.join(equipment_problem_type.name.upper()
                              for equipment_problem_type in
                              self.equipment_problem_types.all()))
                 if self.equipment_problem_types.count()
                 else '') +
                (' (DISMISSED)'
                 if self.dismissed
                 else ''))

    def save(self, *args, **kwargs):
        """Save."""
        self.date_range = \
            DateRange(
                lower=self.from_date,
                upper=self.to_date,
                bounds='[]',
                empty=False)

        self.duration = \
            (self.to_date - self.from_date).days + 1 \
            if self.to_date \
            else None

        super().save(*args, **kwargs)


class AlertDiagnosisStatus(Model):
    """Alert Diagnosis Status."""

    RELATED_NAME = 'alert_diagnosis_statuses'
    RELATED_QUERY_NAME = 'alert_diagnosis_status'

    index = \
        PositiveSmallIntegerField(
            blank=False,
            null=False,
            unique=True,
            default=0,
            db_index=True)

    name = \
        CharField(
            verbose_name='Alert Diagnosis Status Name',
            max_length=MAX_CHAR_LEN,
            blank=False,
            null=False,
            unique=True,
            default='to_diagnose')

    class Meta:
        """Metadata."""

        verbose_name = 'Alert Diagnosis Status'
        verbose_name_plural = 'Alert Diagnosis Statuses'

        ordering = ('index',)

    def __str__(self):
        """Return string repr."""
        return f'{self.index}. {self.name}'

    def save(self, *args, **kwargs):
        """Save."""
        self.name = clean_lower_str(self.name)
        super().save(*args, **kwargs)


class EquipmentInstanceAlertPeriod(Model):
    """Equipment Instance Alert Period."""

    RELATED_NAME = 'equipment_instance_alert_periods'
    RELATED_QUERY_NAME = 'equipment_instance_alert_period'

    equipment_unique_type_group = \
        ForeignKey(
            to=EquipmentUniqueTypeGroup,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    equipment_instance = \
        ForeignKey(
            to=EquipmentInstance,
            related_name=RELATED_NAME,
            related_query_name=RELATED_QUERY_NAME,
            blank=False,
            null=False,
            on_delete=PROTECT)

    risk_score_name = \
        CharField(
            max_length=MAX_CHAR_LEN,
            blank=False,
            null=False,
            unique=False,
            db_index=True)

    threshold = \
        FloatField(
            blank=False,
            null=False,
            default=0,
            db_index=True)

    from_date = \
        DateField(
            blank=False,
            null=False,
            auto_now=False,
            auto_created=False,
            default=None,
            db_index=True)

    to_date = \
        DateField(
            blank=False,
            null=False,
            auto_now=False,
            auto_created=False,
            default=None,
            db_index=True)

    date_range = \
        DateRangeField(
            blank=True,
            null=True)

    duration = \
        IntegerField(
            blank=False,
            null=False,
            default=0)

    cumulative_excess_risk_score = \
        FloatField(
            blank=False,
            null=False,
            default=0)

    approx_average_risk_score = \
        FloatField(
            blank=False,
            null=False,
            default=0)

    last_risk_score = \
        FloatField(
            blank=False,
            null=False,
            default=0)

    ongoing = \
        BooleanField(
            blank=False,
            null=False,
            default=False,
            db_index=True)

    info = \
        JSONField(
            blank=True,
            null=True,
            default=dict)

    diagnosis_status = \
        ForeignKey(
            to=AlertDiagnosisStatus,
            blank=True,
            null=True,
            on_delete=PROTECT)

    equipment_instance_alarm_periods = \
        ManyToManyField(
            to=EquipmentInstanceAlarmPeriod,
            through=(EquipmentInstanceAlarmPeriod
                     .equipment_instance_alert_periods.through),
            related_name=RELATED_NAME + '_reverse',
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    has_associated_equipment_instance_alarm_periods = \
        BooleanField(
            blank=False,
            null=False,
            default=False,
            db_index=True)

    equipment_instance_problem_diagnoses = \
        ManyToManyField(
            to=EquipmentInstanceProblemDiagnosis,
            through=(EquipmentInstanceProblemDiagnosis
                     .equipment_instance_alert_periods.through),
            related_name=RELATED_NAME + '_reverse',
            related_query_name=RELATED_QUERY_NAME,
            blank=True)

    has_associated_equipment_instance_problem_diagnoses = \
        BooleanField(
            blank=False,
            null=False,
            default=False,
            db_index=True)

    class Meta:
        """Metadata."""

        verbose_name = 'Equipment Instance Alert Period'
        verbose_name_plural = 'Equipment Instance Alert Periods'

        unique_together = \
            ('equipment_unique_type_group',
             'equipment_instance',
             'risk_score_name',
             'threshold',
             'from_date'), \
            ('equipment_unique_type_group',
             'equipment_instance',
             'risk_score_name',
             'threshold',
             'to_date')

        ordering = \
            'diagnosis_status', \
            '-ongoing', \
            'risk_score_name', \
            '-threshold', \
            '-cumulative_excess_risk_score'

    def __str__(self):
        """Return string repr."""
        if self.diagnosis_status is None:
            self.save()

        return (
            f'{self.diagnosis_status.name.upper()}: ' +
            ('ONGOING '
             if self.ongoing
             else '') +
            'Alert on ' +
            (f'{self.equipment_unique_type_group.equipment_general_type.name.upper()} '  # noqa: E501
             f'{self.equipment_unique_type_group.name} '
             f'#{self.equipment_instance.name} '
             f'from {self.from_date} to {self.to_date} '
             f'w Approx Avg Risk Score {self.approx_average_risk_score:,.1f} '
             f'(Last: {self.last_risk_score:,.1f}) '
             f'(based on {self.risk_score_name} > {self.threshold}) '
             f'for {self.duration:,} Day(s)')
        )

    def save(self, *args, **kwargs):
        """Save."""
        self.date_range = \
            DateRange(
                lower=self.from_date,
                upper=self.to_date,
                bounds='[]',
                empty=False)

        self.duration = duration = \
            (self.to_date - self.from_date).days + 1

        self.approx_average_risk_score = \
            self.threshold + \
            (self.cumulative_excess_risk_score / duration)

        if self.diagnosis_status is None:
            self.diagnosis_status = \
                AlertDiagnosisStatus.objects.get_or_create(index=0)[0]

        super().save(*args, **kwargs)


def equipment_instance_alarm_period_post_save(
        sender, instance, *args, **kwargs):
    """Post-Save signal."""
    # pylint: disable=unused-argument
    equipment_instance_alert_periods = \
        EquipmentInstanceAlertPeriod.objects.filter(
            equipment_instance=instance.equipment_instance,
            date_range__overlap=instance.date_range)

    instance.equipment_instance_alert_periods.set(
        equipment_instance_alert_periods,
        clear=False)

    equipment_instance_alert_periods.update(
        has_associated_equipment_instance_alarm_periods=True)

    equipment_instance_problem_diagnoses = \
        EquipmentInstanceProblemDiagnosis.objects.filter(
            equipment_instance=instance.equipment_instance,
            date_range__overlap=instance.date_range)

    instance.equipment_instance_problem_diagnoses.set(
        equipment_instance_problem_diagnoses,
        clear=False)

    equipment_instance_problem_diagnoses.update(
        has_associated_equipment_instance_alarm_periods=True)

    EquipmentInstanceAlarmPeriod.objects.filter(pk=instance.pk).update(
        has_associated_equipment_instance_alert_periods=  # noqa: E251
        bool(equipment_instance_alert_periods.count()),

        has_associated_equipment_instance_problem_diagnoses=  # noqa: E251
        bool(equipment_instance_problem_diagnoses.count()))


post_save.connect(
    receiver=equipment_instance_alarm_period_post_save,
    sender=EquipmentInstanceAlarmPeriod,
    weak=True,
    dispatch_uid=None,
    apps=None)


def equipment_instance_alert_period_post_save(
        sender, instance, *args, **kwargs):
    """Post-Save signal."""
    # pylint: disable=unused-argument

    equipment_instance_alarm_periods = \
        EquipmentInstanceAlarmPeriod.objects.filter(
            equipment_instance=instance.equipment_instance,
            date_range__overlap=instance.date_range)

    instance.equipment_instance_alarm_periods.set(
        equipment_instance_alarm_periods,
        clear=False)

    equipment_instance_alarm_periods.update(
        has_associated_equipment_instance_alert_periods=True)

    equipment_instance_problem_diagnoses = \
        EquipmentInstanceProblemDiagnosis.objects.filter(
            equipment_instance=instance.equipment_instance,
            date_range__overlap=instance.date_range)

    instance.equipment_instance_problem_diagnoses.set(
        equipment_instance_problem_diagnoses,
        clear=False)

    equipment_instance_problem_diagnoses.update(
        has_associated_equipment_instance_alert_periods=True)

    EquipmentInstanceAlertPeriod.objects.filter(pk=instance.pk).update(
        has_associated_equipment_instance_problem_diagnoses=  # noqa: E251
        bool(equipment_instance_problem_diagnoses.count()))


post_save.connect(
    receiver=equipment_instance_alert_period_post_save,
    sender=EquipmentInstanceAlertPeriod,
    weak=True,
    dispatch_uid=None,
    apps=None)


def equipment_instance_problem_diagnosis_post_save(
        sender, instance, *args, **kwargs):
    """Post-Save signal."""
    # pylint: disable=unused-argument
    equipment_instance_alarm_periods = \
        EquipmentInstanceAlarmPeriod.objects.filter(
            equipment_instance=instance.equipment_instance,
            date_range__overlap=instance.date_range)

    instance.equipment_instance_alarm_periods.set(
        equipment_instance_alarm_periods,
        clear=False)

    equipment_instance_alarm_periods.update(
        has_associated_equipment_instance_problem_diagnoses=True)

    equipment_instance_alert_periods = \
        EquipmentInstanceAlertPeriod.objects.filter(
            equipment_instance=instance.equipment_instance,
            date_range__overlap=instance.date_range)

    instance.equipment_instance_alert_periods.set(
        equipment_instance_alert_periods,
        clear=False)

    equipment_instance_alert_periods.update(
        has_associated_equipment_instance_problem_diagnoses=True)

    EquipmentInstanceProblemDiagnosis.objects.filter(pk=instance.pk).update(
        has_equipment_problems=bool(instance.equipment_problem_types.count()),

        has_associated_equipment_instance_alarm_periods=  # noqa: E251
        bool(equipment_instance_alarm_periods.count()),

        has_associated_equipment_instance_alert_periods=  # noqa: E251
        bool(equipment_instance_alert_periods.count()))


post_save.connect(
    receiver=equipment_instance_problem_diagnosis_post_save,
    sender=EquipmentInstanceProblemDiagnosis,
    weak=True,
    dispatch_uid=None,
    apps=None)
