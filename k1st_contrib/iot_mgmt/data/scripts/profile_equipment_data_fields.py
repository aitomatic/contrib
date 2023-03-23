"""Profile a specified Equipment Unique Type Group's data fields."""


from pandas._libs.missing import NA   # pylint: disable=no-name-in-module
from tqdm import tqdm

from h1st.contrib.pmfp.data_mgmt import EquipmentParquetDataSet
from h1st.utils.data_proc import ParquetDataset

from h1st_contrib.iot_mgmt.api import (EquipmentUniqueTypeGroup,
                                       EquipmentUniqueTypeGroupDataFieldProfile)   # noqa: E501


MAX_N_DISTINCT_VALUES_TO_PROFILE: int = 30


def run(general_type: str, unique_type_group: str):
    """Run this script to profile Equipment Unique Type Group's data fields."""
    # get Equipment Unique Type Group and corresponding Parquet Data Set
    eq_unq_tp_grp: EquipmentUniqueTypeGroup = \
        EquipmentUniqueTypeGroup.objects.get(name=unique_type_group)

    eq_unq_tp_grp_parquet_data_set: EquipmentParquetDataSet = \
        EquipmentParquetDataSet(general_type=general_type,
                                unique_type_group=unique_type_group)

    eq_unq_tp_grp_parquet_ds: ParquetDataset = \
        eq_unq_tp_grp_parquet_data_set.load()

    # delete previously stored Data Field profiles
    EquipmentUniqueTypeGroupDataFieldProfile.objects.filter(
        equipment_unique_type_group=eq_unq_tp_grp).delete()

    # profile Data Fields and save profiles into DB
    for equipment_data_field in tqdm(eq_unq_tp_grp.equipment_data_fields.all()):   # noqa: E501
        eq_data_field_name: str = equipment_data_field.name

        if eq_data_field_name in eq_unq_tp_grp_parquet_ds.possibleFeatureCols:
            # pylint: disable=protected-access

            if eq_unq_tp_grp_parquet_ds.typeIsNum(eq_data_field_name):
                eq_unq_tp_grp_parquet_ds._nulls[eq_data_field_name] = \
                    equipment_data_field.lower_numeric_null, \
                    equipment_data_field.upper_numeric_null

            _distinct_values_proportions: dict = {
                (str(NA) if k is NA else k): v
                for k, v in
                eq_unq_tp_grp_parquet_ds.distinct(eq_data_field_name).items()}
            _n_distinct_values: int = len(_distinct_values_proportions)

            eq_unq_tp_grp_data_field_profile: \
                EquipmentUniqueTypeGroupDataFieldProfile = \
                EquipmentUniqueTypeGroupDataFieldProfile.objects.create(
                    equipment_unique_type_group=eq_unq_tp_grp,
                    equipment_data_field=equipment_data_field,
                    valid_proportion=(eq_unq_tp_grp_parquet_ds
                                      .nonNullProportion(eq_data_field_name)),
                    n_distinct_values=_n_distinct_values)

            if _n_distinct_values <= MAX_N_DISTINCT_VALUES_TO_PROFILE:
                eq_unq_tp_grp_data_field_profile.distinct_values = \
                    _distinct_values_proportions

            if eq_unq_tp_grp_parquet_ds.typeIsNum(eq_data_field_name):
                quartiles: dict = (eq_unq_tp_grp_parquet_ds
                                   .reprSample[eq_data_field_name]
                                   .describe(percentiles=(.25, .5, .75))
                                   .drop(index='count',
                                         level=None,
                                         inplace=False,
                                         errors='raise')
                                   .to_dict())

                eq_unq_tp_grp_data_field_profile.sample_min = \
                    quartiles['min']
                eq_unq_tp_grp_data_field_profile.outlier_rst_min = \
                    eq_unq_tp_grp_parquet_ds.outlierRstMin(eq_data_field_name)
                eq_unq_tp_grp_data_field_profile.sample_quartile = \
                    quartiles['25%']
                eq_unq_tp_grp_data_field_profile.sample_median = \
                    quartiles['50%']
                eq_unq_tp_grp_data_field_profile.sample_3rd_quartile = \
                    quartiles['75%']
                eq_unq_tp_grp_data_field_profile.outlier_rst_max = \
                    eq_unq_tp_grp_parquet_ds.outlierRstMax(eq_data_field_name)
                eq_unq_tp_grp_data_field_profile.sample_max = \
                    quartiles['max']

            eq_unq_tp_grp_data_field_profile.save()
