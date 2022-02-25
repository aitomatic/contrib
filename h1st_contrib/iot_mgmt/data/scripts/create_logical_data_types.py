"""Create CAT & NUM logical data types."""


from h1st_iot.data_mgmt.models import LogicalDataType


def run():
    """Run this script to create CAT & NUM logical data types."""
    print(msg := 'Creating Categorical & Numerical logical data types...')

    try:
        cat, _ = LogicalDataType.objects.get_or_create(name='cat')
        num, _ = LogicalDataType.objects.get_or_create(name='num')
        print(cat, num)

    except Exception as err:   # pylint: disable=broad-except
        print(f'*** {err} ***')

    print(f'{msg} DONE!\n')
